import bottle
from database_manage import Database_manage_recap
import ast
#from algo_ROI import Algo_roi
# from pricing_procedure import Pricing_procedure
from collections import OrderedDict
import os
from filehandling import File_template_handling
from mail import Email_handler
from bottle import static_file, route, response
import cherrypy
from docgen import DocGen
# connect to mongoDB
connection_string = "mongodb://localhost"
database = Database_manage_recap()
database.connection()

section_interface_dict = {}
question_interface_dict = {}

# bottle.TEMPLATE_PATH.insert(0,'c:\RECAP\src/')

@route('/convertpdf')
@bottle.post('/convertpdf')
def convertpdf():
    print('convertpdf')
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

    if template1==template:
            doc2 = DocGen()
            #company_name = 'Principalx Systems'
            filename = doc2.mail_merge(template, company_data)
            output = filename[:-5]+ '.pdf'
            print(output)
            doc2.convert(filename, output)
            return bottle.template('convertpdf', template = template, message = 'Your pdf: '+ output+' is ready.', company_data = company_data)

    return bottle.template('convertpdf', template = template, company_data = company_data, message ='')


@route('/')
def index():
    #response.charset = 'utf-8'
    return bottle.template('index')


@route('/scrolling')
def scrolling():
    #response.charset = 'utf-8'
    return bottle.template('scrolling')

@route('/map_link')
def map_link():
    #response.charset = 'utf-8'
    return bottle.template('map_link')

@route('/scrolling_doc')
def scrolling_doc():
    #response.charset = 'utf-8'
    section_interface_dict, question_interface_dict = database.create_interface_dict('all')
    return bottle.template('scrolling_doc',form1=section_interface_dict,
                 form2=question_interface_dict)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,
             root='C:\eclipse for python\workspace\RECAP\src\static')


@bottle.route('/download')
def download():
    print('download')
    return bottle.template('download')


@bottle.route('/accordian')
def accordian():
    print('accordion')
    return bottle.template('accordian')


@bottle.route('/document')
def document():
    section_interface_dict, question_interface_dict = database.create_interface_dict('all')
    return bottle.template('document', form1=section_interface_dict,
                 form2=question_interface_dict)


@bottle.route('/user_interface')
def user_interface():
    print('-------******************************-------')
    section_interface_dict, question_interface_dict = database.create_interface_dict('sales')
    #question_interface_dict = database.phase1()
    print(section_interface_dict)
    print(question_interface_dict)
    print('-------******************************-------')
#print('-------ggggggggggggggggggg-------')
    #roi_holder = {'test': 'test'}
#    free_text_list =[]
#    for section_no in range(1,38):
#        free_text_list.append( database.get_free_text(section_no))
#    print (free_text_list)

    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict)


@bottle.route('/scoping')
def scoping():
    print('-------******************************-------')
    section_interface_dict, question_interface_dict = database.create_interface_dict('scoping')
    #question_interface_dict = database.phase1()
    print(section_interface_dict)
    print(question_interface_dict)
    print('-------******************************-------')
#print('-------ggggggggggggggggggg-------')
    #roi_holder = {'test': 'test'}
#    free_text_list =[]
#    for section_no in range(1,38):
#        free_text_list.append( database.get_free_text(section_no))
#    print (free_text_list)

    return bottle.template('tab', form1=section_interface_dict,
                 form2=question_interface_dict)



#def populate_dict_fromdb():
#    #global section_interface_dict
#    #global question_interface_dict
#
#    section_interface_dict,
#    question_interface_dict =
#
#    return section_interface_dict, question_interface_dict

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
    # form = bottle.request.forms.get('answer')
    section_no = bottle.request.forms.get('section')
    free_text = bottle.request.forms.get('free_text')
    print ('free_text here', free_text)

    section_no
    print('section = ', section_no)
    section_no = int(section_no)
    save_free_text(section_no, free_text)
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

    section_interface_dict, question_interface_dict = save_answer(form,  modifier)

    # print(section_interface_dict)
#    free_text_list =[]
#    for section_no in range(1,38):
#        print(section_no)
#        var = database.get_free_text(section_no)
#        print('var',var)
#        free_text_list.append(var )
#    print ('free text',free_text_list)

    return bottle.template("accordian",
             form1=section_interface_dict, form2=question_interface_dict)


def save_free_text(section_no, free_text):
    database.add_free_text(section_no, free_text)


def save_answer(answer_dictionary, modifier):

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

        database.save_answer(question_no, answer)


    return database.create_interface_dict(modifier)


#@bottle.route('/roi_central')
#def roi_central():
#    roi_holder = roi()
#    return bottle.template('roi_central', roi_holder=roi_holder)


#@bottle.route('/roi')
#def roi():
#    print('/roi')
#    # total_roi ={}
#
#    algo = Algo_roi()
#    algo.producivity_saving()
#    algo.error_reduction_saving()
#    algo.total_roi()
#    # print ('tots',total_roi)
#    roi_holder = algo.print_algo_roi()
#
#    return bottle.template('roi', roi_holder=roi_holder)


# @bottle.route('/roi1')
# def roi1():
#    print('/roi1')
#    return bottle.template('roi1', roi1_holder={'q': 'a'})
#
#
# @bottle.route('/roi_list')
# def roi_list():
#    print('roi_list')
#    return bottle.template('roi_list')

# @bottle.route('/roi_recalculate')
# @bottle.post('/roi_recalculate')
# def roi_recalculate():
#    print('roi_recalculate')
#
#    """
#    m method to do this conversion is called
#    """
#
#    roi_dictionary = form_input_parse(bottle.request.forms.get('roi_holder'))
#
#    print(roi_dictionary)
#    return bottle.template('roi_recalculate', roi_holder=roi_dictionary)

@bottle.route('/pricing')
def pricing():
    # print('pricing')
    final_pricing = 666
    return bottle.template('pricing', pricing_holder=final_pricing)


# @bottle.post('/pricing_calculate')
# def pricing_calculate():
#    #print('pricing_calc')
#
#    carpark = bottle.request.forms.get('carpark')
#    currency = bottle.request.forms.get('currency')
#    #print(carpark, currency)
#    pricing1 = Pricing_procedure()
#    pricing1.set_pricing(carpark, currency)
#    pricing1.pricelist_import()
#    pricing_document = pricing1.total_price()
#    total_price = pricing1.price_print()
#    return bottle.template('pricing_calc', pricing_holder=(carpark, currency,
#     pricing_document))


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
    print('start document creation')
    section = bottle.request.forms.get('section')
    print(section)
    text_box = bottle.request.forms.get('text_box')
    print(text_box)
    #document_dict = database.create_interface_dict('sales')
    return bottle.template('doc_create', section = section, text_box = text_box)


bottle.debug(True)
bottle.run(server='cherrypy', host='localhost', port=8081)
# bottle.run(server = 'cherrypy',host='0.0.0.0', port=8081 )
