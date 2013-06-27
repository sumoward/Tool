import bottle
from database_manage import Database_manage_recap
import ast
import user
import cgi
from collections import OrderedDict
import os
from filehandling import File_template_handling
from mail import Email_handler
from bottle import static_file, route, error, response
from docgen import DocGen
from pymongo.mongo_client import MongoClient

# connect to mongoDB
connection_string = "mongodb://localhost"
database = Database_manage_recap()
#database.connection()

section_interface_dict = {}
question_interface_dict = {}


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
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
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

    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    if (user.validate_signup(username, password, verify, email, errors)):
        if (not user.newuser(connection, username, password, email)):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)

        session_id = user.start_session(connection, username)
        print ('sessionid', session_id)
        cookie = user.make_secure_val(session_id)
        bottle.response.set_cookie("session", cookie)
        cook = bottle.request.get_cookie('session')
        print('cook',cook)
        print('user',username)
        #username = bottle.request.forms.get("username")
        return bottle.template("welcome" , username=username)
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
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print ("user submitted ", username, "pass ", password)

    userRecord = {}
    if (user.validate_login(connection, username, password, userRecord)):
        session_id = user.start_session(connection, username)
        if (session_id == -1):
            bottle.redirect("/internal_error")

        cookie = user.make_secure_val(session_id)

        # Warning, if you are running into a problem whereby the cookie being set here is 
        # not getting set on the redirect, you are probably using the experimental version of bottle (.12). 
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
    if (cookie == None):
        print ("no cookie...")
        bottle.redirect("/signup")
    else:
        session_id = user.check_secure_val(cookie)
        if (session_id == None):
            print ("no secure session_id")
            bottle.redirect("/signup")
        else:
            # remove the session
            user.end_session(connection, session_id)
            print ("clearing the cookie")
            bottle.response.set_cookie("session","")
            bottle.redirect("/signup")

@route('/convertpdf')
@bottle.post('/convertpdf')
def convertpdf():
    print('convertpdf-----------------------')
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    company_data = {'Title': 'Mr',
                        'First_Name': 'Joe',
                        'Last_Name': 'OShea',
                        'Company_Name': 'Principal Systems',
                        'Email_Address': 'joeoshea@principalsystems.com',
                        'City': 'Dublin',
                        'State': 'Dublin',
                        'Work_Phone': '123333',
                        'Address_Line_1': '56 Pembrooke road',
                        'Address_Line_2': 'Ballsbridge',
                        'Home_Phone': '1234567',
                        'Country_or_Region': 'Ireland',
                        'ZIP_Code': 'Dublin6'}

    template1 = bottle.request.forms.get('template')
    print('T!', template1)
    template = 'Executive_Summary2.docx'
    print (template)

    if template1 == template:
            doc2 = DocGen()
            #company_name = 'Principalx Systems'
            filename = doc2.mail_merge(template, company_data)
            output = filename[:-5]+ '.pdf'
            print(output)
            doc2.convert(filename, output)
            return bottle.template('convertpdf', template = template, message = 'Your pdf: '+ output+' is ready.', company_data = company_data)

    return bottle.template('convertpdf', template = template, company_data = company_data, message ='', username=username)


@route('/')
def index():
    print('Check Login')
    username = login_check()  # see if user is logged in
    if (username is None):
        bottle.redirect("/login")
    session = bottle.request.get_cookie('session')
    print ('user',username, ':', session)
    #response.charset = 'utf-8'
    return bottle.template('scrolling', username=username)

@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return ({error:"System has encountered a DB error"})


@route('/scrolling')
def scrolling():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")

    #response.charset = 'utf-8'
    return bottle.template('scrolling', username=username)

@route('/map_link')
def map_link():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    #response.charset = 'utf-8'
    return bottle.template('map_link', username=username)


@route('/scrolling_doc')
def scrolling_doc():
    #response.charset = 'utf-8
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    print('useer',username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('all', username)
    return bottle.template('scrolling_doc',
                form1=section_interface_dict,
                 form2=question_interface_dict, username=username)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,
             #root='.\static')
            root='/home/ubuntu/recap/RECAP/src')


@bottle.route('/download')
def download():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    print('download')
    return bottle.template('download')


@bottle.route('/accordian')
def accordian():
    print('accordion')
    return bottle.template('accordian')


@bottle.route('/document')
def document():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    section_interface_dict, question_interface_dict = database.create_interface_dict('all')
    return bottle.template('document', form1=section_interface_dict,
                 form2=question_interface_dict)


@bottle.post('/user_interface')
@bottle.route('/user_interface')
def user_interface():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    #username = bottle.request.forms.get("username")
    print(username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('sales', username)
    #username = bottle.request.forms.get("username")
    cook = bottle.request.get_cookie('session')
    #print('cook-interface',cook)
    #question_interface_dict = database.phase1()
    #print(section_interface_dict)
    #print(question_interface_dict)
    #print('-------******************************-------')

    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict,
                 username=username)


@bottle.route('/scoping')
def scoping():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    section_interface_dict, question_interface_dict = database.create_interface_dict('scoping', username)
    #question_interface_dict = database.phase1()
    print(section_interface_dict)
    print(question_interface_dict)
    print('-------******************************-------')
    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict, username=username)


@bottle.route('/section/<section>')
def section(section):
    print('section test script')
    # plain_text = bottle.request.forms.get('form')
    return bottle.template('form1', form=section)


@bottle.route('/accordian2')
def accordian2():
    print('accordian2====================================================')
    return bottle.template('accordian2', form1='form holder string')


@bottle.route('/form_end')
@bottle.post('/form_end')
def form_end():
    print('-------******************************-------')
    print('form_end')
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    #print('-------******************************-------')
    database = Database_manage_recap()
    database.dbconnection(username)
    #username = bottle.request.forms.get("username")
    print(username)
    # form = bottle.request.forms.get('answer')
    section_no = bottle.request.forms.get('section')
    free_text = bottle.request.forms.get('free_text')
    print ('free_text here', free_text, username)
    print('section = ', section_no)
    section_no = int(section_no)
    save_free_text(section_no, free_text, username)
    no_questions = database.count_questions(section_no)

    if section_no < 13:
        modifier = 'sales'
    else:
        modifier ='scoping'

    form = {}
    for x in range(no_questions):
        x = (section_no * 1000) + (x + 1)
        x = str(x)
        # print('x',x)
        form[x] = bottle.request.forms.get(x)

    section_interface_dict, question_interface_dict = save_answer(form,  modifier, username)

    return bottle.template("tab",
             form1=section_interface_dict, form2=question_interface_dict, username=username)


def save_free_text(section_no, free_text, username):
    database.add_free_text(section_no, free_text, username)


def save_answer(answer_dictionary, modifier, username):

    for key in answer_dictionary.keys():
        # print(answer_dictionary
        question_no = int(key)
        # print(question_no)
        answer = answer_dictionary[key]
        # print(answer)
        # check if the answer should be stored as an int
        try:
            answer = int(answer)
        except ValueError:
            print('will not convert to an int')
        print('saving.....')
        database.save_answer(question_no, answer,username)


    return database.create_interface_dict(modifier, username)

@bottle.route('/pricing')
def pricing():
    # print('pricing')
    final_pricing = 666
    return bottle.template('pricing', pricing_holder=final_pricing)


@bottle.route('/saved_file')
@bottle.post('/saved_file')
def saved_file():
    print('save_file')

    data = bottle.request.files.uploadField
    print(data)

    if data and data.file:
        raw = data.file.read()  # This is dangerous for big files
        print(raw)
        filename = data.filename
        form = "Hello ! You uploaded %s (%d bytes)." % (filename, len(raw))
        print(form)

        # save the file

        target_dir = r"static/uploaded"

        filename = os.path.join(target_dir, filename)
        print(filename)
        # write the uploaded file to the storage
        fileObj = open(filename, "wb")
        fileObj.write(data.value)
        fileObj.close()
        print(filename, ' writen to file.')
        # email the user to inform that a file has been uploaded
        handler = Email_handler()
        handler.build_mime(filename)

        return bottle.template('saved_file', form=filename)

    return bottle.template('saved_file', form='empty')


@bottle.post('/documentation')
@bottle.route('/documentation')
def documentation():
    print('documentation')
    uploaded_file = bottle.request.forms.get('doc_upload')
    downloaded_file = bottle.request.forms.get('document_download')

    if downloaded_file:
        print(downloaded_file)
        # use the file handling class
        file_handler = File_template_handling()
        file_handler.directory()
        if downloaded_file == 't1':
            filename = 'static/downloads/ASN & Pallet and Case Label Data Capture Template.xlsx'
        elif downloaded_file == 't2':
            filename = 'static/downloads/BRC Data Capture Template.xlsx'
        elif downloaded_file == 't3':
            filename = 'static/downloads/Customer charges.xlsx'
        elif downloaded_file == 't4':
            filename = 'static/downloads/In-DEX User Profiles Data Capture Template.xlsx'
        elif downloaded_file == 't5':
            filename = 'static/downloads/In-DEX WMS Functionality Checklist.xls'
        elif downloaded_file == 't6':
            filename = 'static/downloads/Master Charges.xlsx'
        elif downloaded_file == 't7':
            filename = 'static/downloads/Product Code Data Capture Template.xlsx'

        target_dir = r"C:\eclipse for python\workspace\RECAP\src/"
        print('filename: ' + filename)
        filename = os.path.join(target_dir, filename)

        # open the file using the associated software

        os.startfile(filename)
        print('opened : ' + filename)
        print(' the following was sent', uploaded_file, downloaded_file)
        return bottle.template('download')
    else:
        return bottle.template('upload')
    """
    convert the string back to an ordered dict
    """


def form_input_parse(form_dictionary):
    print('form input parse')
    # remove the word Ordered Dict
    form_dictionary = form_dictionary[11:]
    # evaluate the remaining string
    # print(form_dictionary)
    form_dictionary = ast.literal_eval(form_dictionary)

    d = OrderedDict()
    for x, y in form_dictionary:
        d.setdefault(x, y)
    print (d)
    form_dictionary = d
    # print ('form_end')
    # populate the Dictionary with inputs
    for key  in form_dictionary:
        # print('key: ',key)
        form_dictionary[key] = bottle.request.forms.get(key)
        # print(bottle.request.forms.get(key))
        print('end form parse', form_dictionary)

    return form_dictionary


@bottle.post('/doc_create')
@bottle.route('/doc_create')
def create_doc():
    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")
    print('start document creation')
    section = bottle.request.forms.get('section')
    print(section)
    text_box = bottle.request.forms.get('text_box')
    print(text_box)
    #document_dict = database.create_interface_dict('sales')
    return bottle.template('doc_create', section = section, text_box = text_box, username=username)


bottle.debug(True)
#bottle.run(server='cherrypy', host='localhost', port=8081)
bottle.run(server = 'cherrypy',host='0.0.0.0', port=8081 )
