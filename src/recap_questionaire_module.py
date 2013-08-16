"""
ReCap is a tool to gather sales and scoping information for Principal systems.

This is the bottle server running on CherryPy

"""
import bottle
from database_manage import Database_manage_recap
import ast
import user
import cgi
from collections import OrderedDict
import os
from filehandling import File_template_handling
from mail import Email_handler
from bottle import static_file, route, error, response, template
from docgen import DocGen
from pymongo.mongo_client import MongoClient
from pricing_procedure import Pricing_procedure
import pymongo


# connect to mongoDB
connection_string = "mongodb://localhost"
database = Database_manage_recap()
#database.connection()

section_interface_dict = {}
question_interface_dict = {}
#set the maximum number of post vars passed
bottle.BaseRequest.MAX_PARAMS = 150


# will check if the user is logged in and if so, return the username.
# otherwise,it returns None
def login_check():
    connection = MongoClient("localhost", 27017)
    cookie = bottle.request.get_cookie("session")
    if (cookie == None):
        print ("no cookie...")
        return None
    else:
        session_id = user.check_secure_val(cookie)
        if (session_id == None):
            print ("no secure session_id")
            return None
        else:
            # look up username record
            session = user.get_session(connection, session_id)
            if (session == None):
                return None
    return session['username']


@bottle.get("/welcome")
def present_welcome():
    # check for a cookie, if present, then extract value
    username = login_check()
    print(len(username))
    if (username is None):
        redirect()
    return bottle.template("welcome", {'username': username})


# displays the initial recap signup form
@bottle.get('/signup')
def present_signup():
    return bottle.template("signup",
                           dict(username="", password="",
                                password_error="",
                                email="", username_error="", email_error="",
                                verify_error=""))


@bottle.post('/signup')
def process_signup():
    print('signup process')
    connection = MongoClient("localhost", 27017)

    email = bottle.request.forms.get("email").strip()
    username = bottle.request.forms.get("username").strip()
    password = bottle.request.forms.get("password").strip()
    verify = bottle.request.forms.get("verify").strip()
    
    print(email,username,password,verify)

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    print('er:', errors)
    if (user.validate_signup(username, password, verify, email, errors)):
        print('here1')
        if (not user.newuser(connection, username, password, email)):
            # this was a duplicate
            print('dup')
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)

        session_id = user.start_session(connection, username)
        print ('sessionid', session_id)
        cookie = user.make_secure_val(session_id)
        bottle.response.set_cookie("session", cookie)
        #cook = bottle.request.get_cookie('session')
        #print('cook', cook)
        #print('user', username)
        #username = bottle.request.forms.get("username")
        return bottle.template("welcome", username=username)
    else:
        print ("user did not validate")
        return bottle.template("signup", errors)


# displays the initial recap login form
@bottle.get('/login')
def present_login():
    return bottle.template("login",
                           dict(username="", password="",
                                login_error=""))


# handles a login request
@bottle.post('/login')
def process_login():

    connection = MongoClient("localhost", 27017)
    #print('login request')
    username = bottle.request.forms.get("username").strip()
    password = bottle.request.forms.get("password").strip()

    print ("user submitted ", username, "pass ", password)
    print(len(username))

    userRecord = {}
    if (user.validate_login(connection, username, password, userRecord)):
        session_id = user.start_session(connection, username)
        if (session_id == -1):
            bottle.redirect("/internal_error")

        cookie = user.make_secure_val(session_id)

        # Warning, if you are running into a problem
        # whereby the cookie being set here is
        # not getting set on the redirect,
        #you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie("session", cookie)
        bottle.redirect("/welcome")

    else:
        return bottle.template("login",
                           dict(username=cgi.escape(username), password="",
                                login_error="Invalid Login"))


@bottle.get('/logout')
def process_logout():
    connection = MongoClient("localhost", 27017)
    cookie = bottle.request.get_cookie("session")
    if (cookie is None):
        print ("no cookie...")
    else:
        session_id = user.check_secure_val(cookie)
        if (session_id == None):
            print ("no secure session_id")
        else:
            # remove the session
            user.end_session(connection, session_id)
            print ("clearing the cookie")
            bottle.response.set_cookie("session", "")
    bottle.redirect("/signup")     

@route('/convertpdf')
@bottle.post('/convertpdf')
def convertpdf():
    print('convertpdf-----------------------')
    username = login_check()
    if (username is None):
        redirect()

    template1 = bottle.request.forms.get('title')
    template2 = bottle.request.forms.get('first_name')
    template3 = bottle.request.forms.get('last_name')
    template4 = bottle.request.forms.get('company_name')
    template5 = bottle.request.forms.get('email')
    template6 = bottle.request.forms.get('home_phone')
    template7 = bottle.request.forms.get('work_phone')
    template8 = bottle.request.forms.get('addr1')
    template9 = bottle.request.forms.get('addr2')
    template10 = bottle.request.forms.get('country')
    template11 = bottle.request.forms.get('city')
    template12 = bottle.request.forms.get('state')

    company_data = {'Title': template1,
                        'First_Name': template2,
                        'Last_Name': template3,
                        'Company_Name': template4,
                        'Email_Address': template5,
                        'City': template6,
                        'State': template7,
                        'Work_Phone': template8,
                        'Address_Line_1': template9,
                        'Address_Line_2': template10,
                        'Home_Phone': template11,
                        'Country_or_Region': template12
                        }

    #template = 'static/documents/Executive_Summary2.docx'
    template = 'static/documents/templatecust.docx'
    #print ('template is : ', template)

    if template1:
        doc2 = DocGen()
        filename = doc2.mail_merge(template, company_data)
        output = 'static/documents/' + filename[:-5] + '.pdf'
        #print('$$output', output)
        doc2.convert(filename, output)
        #create email handeler
        handler = Email_handler()
        customer = company_data['Email_Address']
        output_filename = []
        output_filename.append(output)
        #print(customer, output_filename)
        handler.build_mime(output_filename, customer)
        return bottle.template('convertpdf', template=template,
                            message='Your document: ' + output + ' is ready. A copy has been emailed to you',
                                         company_data=company_data,
                                        username=username)

    return bottle.template('convertpdf', template=template, company_data=company_data, message='', username=username)


@route('/')
def index():
    print('Check Login')
    username = login_check()  # see if user is logged in
    if (username is None):
        bottle.redirect("/login")
    #session = bottle.request.get_cookie('session')
    #print ('user',username, ':', session)
    #response.charset = 'utf-8'
    return bottle.template('scrolling', username=username)


@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return ({error: "System has encountered a DB error"})


@route('/scrolling')
def scrolling():
    username = login_check()
    if (username is None):
        redirect()
    #response.charset = 'utf-8'
    return bottle.template('scrolling', username=username)


@route('/map_link')
def map_link():
    username = login_check()
    if (username is None):
        redirect()
    #response.charset = 'utf-8'
    return bottle.template('map_link', username=username)


@route('/scrolling_doc')
def scrolling_doc():
    #response.charset = 'utf-8
    username = login_check()
    if (username is None):
        redirect()
    #print('useer',username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('all', username)
    return bottle.template('scrolling_doc',
                form1=section_interface_dict,
                 form2=question_interface_dict, username=username)


@route('/unanswered')
def unanswered():
    username = login_check()
    if (username is None):
        redirect()
    section_interface_dict, question_interface_dict = database.create_interface_dict('all', username)
    return bottle.template('unanswered',
                form1=section_interface_dict,
                 form2=question_interface_dict, username=username)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,
             #root='.\static')
             root='/home/ubuntu/recap/RECAP/src/static')


@bottle.post('/download')
@bottle.route('/download')
def download():
    username = login_check()
    if (username is None):
        redirect()
    print('download')
    return bottle.template('download', username=username, message="")


@bottle.route('/accordian')
def accordian():
    #print('accordion')
    return bottle.template('accordian')


@bottle.route('/document')
def document():
    username = login_check()
    if (username is None):
        redirect()
    section_interface_dict, question_interface_dict = database.create_interface_dict('all')
    return bottle.template('document', form1=section_interface_dict,
                 form2=question_interface_dict)


@bottle.post('/user_interface')
@bottle.route('/user_interface')
def user_interface():
    username = login_check()
    if (username is None):
        redirect()
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    #username = bottle.request.forms.get("username")
    #print(username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('sales', username)
    #username = bottle.request.forms.get("username")
    #cook = bottle.request.get_cookie('session')
    #print('cook-interface',cook)
    #question_interface_dict = database.phase1()
    #print(section_interface_dict)
    #print(question_interface_dict)
    #print('-------******************************-------')

    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict,
                 username=username)


@bottle.post('/professional_services')
@bottle.route('/professional_services')
def professional_services():
    username = login_check()
    if (username is None):
        redirect()
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('prof', username)
    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict,
                 username=username)


@bottle.route('/scoping')
def scoping():
    username = login_check()
    if (username is None):
        redirect()
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('scoping', username)
    #question_interface_dict = database.phase1()
    #print(section_interface_dict)
    #print(question_interface_dict)
    #print('-------******************************-------')
    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict, username=username)


@bottle.route('/section/<section>')
def section(section):
    print('section test script')
    # plain_text = bottle.request.forms.get('form')
    return bottle.template('form1', form=section)


@bottle.route('/accordian2')
def accordian2():
    #print('accordian2====================================================')
    return bottle.template('accordian2', form1='form holder string')


@bottle.route('/form_end')
@bottle.post('/form_end')
def form_end():
    #print('-------******************************-------')
    print('form_end')
    username = login_check()
    if (username is None):
        redirect()
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    #username = bottle.request.forms.get("username")
    print(username)
    # form = bottle.request.forms.get('answer')
    section_no = bottle.request.forms.get('section')
    free_text = bottle.request.forms.get('free_text')
    #print ('free_text here', free_text, username)
    #print('section = ', section_no)
    section_no = int(section_no)
    save_free_text(section_no, free_text, username)
    no_questions = database.count_questions(section_no)
    #print('no questions',no_questions)

    if section_no < 13:
        modifier = 'sales'
    elif section_no > 45:
        modifier = 'prof'
    else:
        modifier = 'scoping'

    form = {}
    for x in range(no_questions):
        x = (section_no * 1000) + (x + 1)
        #print(x)
        x = str(x)
        #print('x',x)
        form[x] = bottle.request.forms.get(x)
        #print(x,form[x])

    section_interface_dict, question_interface_dict = save_answer(form,  modifier, username)

    return bottle.template("tab",
             form1=section_interface_dict, form2=question_interface_dict, username=username)


def save_free_text(section_no, free_text, username):
    database.add_free_text(section_no, free_text, username)


def save_answer(answer_dictionary, modifier, username):
    for key in answer_dictionary.keys():
        #print(answer_dictionary)
        question_no = int(key)
        print(question_no)
        answer = answer_dictionary[key]
        #print(answer)
        # check if the answer should be stored as an int
        if answer is not None:
            try:
                answer = int(answer)
            except ValueError:
                print('will not convert to an int')
            print('saving.....')
        database.save_answer(question_no, answer, username)
    return database.create_interface_dict(modifier, username)


@bottle.route('/saved_file')
@bottle.post('/saved_file')
def saved_file():
    print('save_file')
    data = bottle.request.files.uploadField
    #print(data)
    if data and data.file:
        raw = data.file.read()  # This is dangerous for big files
        #print(raw)
        filename = data.filename
        #form = "Hello ! You uploaded %s (%d bytes)." % (filename, len(raw))
        #print(form)
        # save the file
        target_dir = r"static/uploaded"
        filename = os.path.join(target_dir, filename)
        #print(filename)
        # write the uploaded file to the storage
        fileObj = open(filename, "wb")
        fileObj.write(data.value)
        fileObj.close()
        #print(filename, ' writen to file.')
        # email the user to inform that a file has been uploaded
        handler = Email_handler()
        handler.build_mime(filename)
        return bottle.template('saved_file', form=filename)

    return bottle.template('saved_file', form='empty')


@bottle.post('/documentation')
@bottle.route('/documentation')
def documentation():
    username = login_check()
    if (username is None):
        redirect()
    print('documentation')
    customer = bottle.request.forms.get('customer')
    downloaded_file = []
    downloaded_file = bottle.request.forms.getlist('document_download')
    #print('downloaded file', downloaded_file)

    if not downloaded_file or not customer:
        print('here', customer, downloaded_file)
        message = "Please select a document and assign an email address to the client"
        return bottle.template('download', username=username, message=message)

    if downloaded_file:
        print('downloaded file', downloaded_file)
        # use the file handling class
        file_handler = File_template_handling()
        list_of_files = file_handler.directory()
        #num = len(list_of_files)
        #print(num)
        filename = []
        for choice in downloaded_file:
            #print('choice',choice)#
            file = 'static/downloads/' + list_of_files[int(choice)]
            #print(file)
            filename.append(file)
            #print(filename)

        target_dir = r"C:\eclipse for python\workspace\RECAP\src/"
        #print('filename: ' , filename)
        #filename = os.path.join(target_dir, filename)
        # open the file using the associated software
        #os.startfile(filename)
        #print('opened : ' , filename)
        print(' the following was sent', downloaded_file)
        #email the file to user
        handler = Email_handler()
        filename = filename
        handler.build_mime(filename, customer)

        message = (str(filename) + ' sent to, ' + customer)
        return bottle.template('download', username=username, message=message)

    """
    convert the string back to an ordered dict
    """


def form_input_parse(form_dictionary):
    #print('form input parse')
    # remove the word Ordered Dict
    form_dictionary = form_dictionary[11:]
    # evaluate the remaining string
    # print(form_dictionary)
    form_dictionary = ast.literal_eval(form_dictionary)

    d = OrderedDict()
    for x, y in form_dictionary:
        d.setdefault(x, y)
    #print (d)
    form_dictionary = d
    # print ('form_end')
    # populate the Dictionary with inputs
    for key  in form_dictionary:
        # print('key: ',key)
        form_dictionary[key] = bottle.request.forms.get(key)
        # print(bottle.request.forms.get(key))
        #print('end form parse', form_dictionary)

    return form_dictionary


@bottle.post('/doc_create')
@bottle.route('/doc_create')
def create_doc():
    username = login_check()
    if (username is None):
        redirect()
    #print('start document creation')
    section = bottle.request.forms.get('section')
    #print(section)
    text_box = bottle.request.forms.get('text_box')
    #print(text_box)
    #document_dict = database.create_interface_dict('sales')
    return bottle.template('doc_create', section=section,
                            text_box=text_box, username=username)


def redirect():
    print ("welcome: can't identify user...redirecting to signup")
    bottle.redirect("/signup")

@bottle.route('/pricing_main')
def pricing_main():
    print('pricing_main')
    username = login_check()
    #print(len(username))
    if (username is None):
        redirect()
    #section_no= 1
    #username ='brian'
    pricing1 = Pricing_procedure()
    pricelist3, overall_total = pricing1.get_totals( username)
    print(pricelist3)
    return bottle.template('pricing_main', sectiontotal='test for section total', username = username, pricelist=pricelist3, overall_total = overall_total)

@bottle.post('/pricing_calc')
def pricing_calc():
    print('pricing_calc')
    username = login_check()
    #print(len(username))
    if (username is None):
        redirect() 
    #retrieve information from price calculator
    edited_values = []
    edited_values = bottle.request.forms.getlist('quantity')
    section_no = bottle.request.forms.get('section_no')
    print (edited_values)
    print (section_no)
    pricing1 = Pricing_procedure()
    pricing1.apply_calc(edited_values, section_no, username)
    pricing1 = Pricing_procedure()
    pricelist3, overall_total = pricing1.get_totals( username)
    print(pricelist3)
    bottle.redirect('/pricing/' + section_no)
    

#@bottle.post('/pricing/<section_no>')
@bottle.route('/pricing/<section_no>')
def pricing_section(section_no):
    print('pricing_section', section_no)
    username = login_check()
    #print(len(username))
    if (username is None):
        redirect()

    index_costs = bottle.request.forms.get('index_costs')
    if not index_costs:
        index_costs = ""

    pricing1 = Pricing_procedure()
    #username = username + '_pricing'
    # check if the pricing template has been generated
    # if not generate the pricing in list
    if  not pricing1.check_pricing_exist(username):
        pricelist1 = pricing1.set_pricing(username)
        print ('check', pricelist1)
    #section_no = 1
    pricelist2 = pricing1.get_pricing(section_no, username)
    print ('p2  for sections', pricelist2)

    return template('pricing', pricelist=pricelist2, section_no=section_no, username=username)
    #return template('Hello {{section_no}}, how are you?',section_no =section_no)

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)



@bottle.post('/best_practice')
@bottle.route('/best_practice')
def best_practice():
    print('best practice')
    message = ""
    first_name = bottle.request.forms.get('form0')
    last_name = bottle.request.forms.get('form1')
    email = bottle.request.forms.get('form2')
    company = bottle.request.forms.get('form3')
    phone = bottle.request.forms.get('form4')
    print(first_name, last_name, email, company)
    if email:
        handler = Email_handler()
        filename = ['static/downloads/Customer charges.xlsx']
        #update the marketing campaign details
        marketing_campaign = 'first one'
        handler.build_mime(filename, email)
        message = (str(filename) + ' sent to, ' + email)
        print('message')
        #connect to recap and store
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection['recap']
        #date time
        db['marketing'].insert({'first_name':first_name,
                                 'last_name':last_name,'email':email, 'company':company,
                                  'phone':phone, 'marketing_campaign':marketing_campaign })
        return bottle.template('best_practice', message = message)
    else:
        message = "Please fill in the details above so that we may send you your information"
        return bottle.template('best_practice', message = message)


#
#bottle.run(server='cherrypy', host='localhost', port=8081)
bottle.run(server='cherrypy', host='0.0.0.0', port=80)
