"""
    interface with the mongo database to allow changes
"""


import bottle
from database_manage import Database_manage_recap
import ast

# connect to mongoDB
connection_string = "mongodb://localhost"
database = Database_manage_recap()
database.connection()


@bottle.post('/')
@bottle.route('/')
def menu():
    print('menu')
    # reloads each time( dsorry testing purposes
    cursor = database.copy_template()
    return bottle.template('menu')


@bottle.post('/create_tag_names')
@bottle.route('/create_tag_names')
def create_tag_names():
    print('create_tag_names')

    tag_array = database.get_list_tag_names()
    print('tag_array', tag_array)
    choice = None
    choice = bottle.request.forms.get('choice')
    print('choice', choice)
    if choice == 'remove':
        print('remove')
        print('tag_name_remove---------------')
        tag_name_remove = bottle.request.forms.get('tag_name_remove')
        print('tag_name_remove', tag_name_remove)
        tag_array = database.remove_tag_name_array(tag_name_remove)
        return bottle.template('create_tag_names', tag_array=tag_array)
    elif choice == 'add':
        print('add')
        new_tag = bottle.request.forms.get('new_tag_name')
        print('new_tag', new_tag)
        tag_array = database.create_new_tag(new_tag)
        return bottle.template('create_tag_names', tag_array=tag_array)

    return bottle.template('create_tag_names', tag_array=tag_array)


@bottle.post('/account_details')
@bottle.route('/account_details')
def account_details():
    print('account details')
    account_details = database.get_account_name()
    print('account details', account_details)
    new_account_name = bottle.request.forms.get('new_account_name')
    print('#new_account_name', new_account_name)
    database.update_account_name(account_details, new_account_name)
    account_details = database.get_account_name()
    return bottle.template('account_details', account_details=account_details)


@bottle.route('/list_tags')
@bottle.post('/list_tags')
def list_tags():
    print('list tags')
    cursor = database.get_sections_and_tags()
    print(cursor)
    section_tag = {}
    for i, x in enumerate(cursor):
        i = i + 1
        section_tag[i] = get_section_tags(i)

    print('section tags :', section_tag)
    return bottle.template('tags_template_for_mongo',
             cursor=cursor, section_tag=section_tag)


@bottle.route('/process_tags')
@bottle.post('/process_tags')
def process_tags():
    print('*' * 80)
    print('tags$$$$$$$$$$$$')
    section = bottle.request.forms.get('form_name')
    print('#section', section)

    # print(isinstance(section, int))

    if section != None:
        section = int(section)

    print('#section:', section)
    choice = bottle.request.forms.get('choice')
    print('#choice', choice)

    if choice == 'add section tag':
        print('add------------------')

        tags, section = add_section_tag()
        print(section, '--------')

        cursor = database.get_sections_and_tags()

        return bottle.template('tags_template_for_mongo' , cursor=cursor)

    elif choice == 'add':
        section = bottle.request.forms.get('section')
        print('section-----', section)
        tags, sections = add_question_tag()
        print('section--tags--', section, tags)
        return bottle.template('tags_edit', tags=tags, section=section)

    elif choice == 'remove':
        print('remove------------------')

        section = bottle.request.forms.get('section')
        print('section-----', section)

        section, tags = remove_question_tag()
        return bottle.template('tags_edit' , tags=tags, section=section)

    elif choice == 'remove section tags':
        print('removest------------------')
        section, tags = remove_section_tag()
        cursor = database.get_sections_and_tags()

        return bottle.template('tags_template_for_mongo', cursor=cursor)

    tags = get_question_tags(section)
    print('------------------')
    print('tags', tags)
    print('------------------')
    return bottle.template('tags_edit', tags=tags, section=section)


@bottle.route('/list_quesions')
@bottle.post('/list_quesions')
def list_questions():
    pass
    cursor = database.get_sections()
    return bottle.template('questions_template_for_mongo', cursor=cursor)


@bottle.route('/process_sections')
@bottle.post('/process_sections')
def process_sections():

    cursor = database.get_sections()
    print('this :', cursor)
    print('*' * 40)

    choice = bottle.request.forms.get('choice')
    print('^^choice is :', choice)
    section = bottle.request.forms.get('form_name')
    if section != None:
        section = int(section)
    print('^^section', section)

    if choice == 'remove':
        print('remove')
        print('^^section^^', section)
        database.remove_section(section)
        print('section removed')
        sections = database.get_sections()
        return bottle.template('section_template_for_mongo', cursor=sections)

    elif choice == 'edit':
        print('edit')

        query_string = 'section_edit_'
        read_in_dict = readin(cursor, query_string)
        print('read_in', read_in_dict)
        sections = edit_sections(read_in_dict, cursor)

        return bottle.template('section_template_for_mongo', cursor=sections)

    elif choice == 'add':
        print('add----')
        if section == None:
            section = len(cursor)
            print('len', section)
        new_section_name = bottle.request.forms.get('new_section')
        sections = add_section(new_section_name, section)
        print('     ', sections)
        return bottle.template('section_template_for_mongo', cursor=sections)

    return bottle.template('section_template_for_mongo', cursor=cursor)


@bottle.route('/process_questions')
@bottle.post('/process_questions')
def process_questions():
    print('*' * 40)
    print('process questions')

    section = bottle.request.forms.get('section')
    print('#section', section)

    quest_no = bottle.request.forms.get('form_name')
    print('#quest_no', quest_no)

    choice = bottle.request.forms.get('choice')
    print('#choice', choice)

    questions = database.get_questions(quest_no)
    # APPEND AN EMPTY QUESTION SLOT FOR EDITING PURPOSES
    # questions.append('')
    print ('questions:', questions)

    return bottle.template('questions_edit', cursor=questions,
                            section=quest_no)


def readin(questions, query_string):

        dict1 = {}
        for i, x in enumerate(questions):
            query = query_string + str(i)
            # print(x, query)
            holder = bottle.request.forms.get(query)
            # print('holder',holder)
            if i != holder:
                dict[i + 1] = holder
        print('dict', dict1)
        return dict1


@bottle.post('/update_questions')
@bottle.route('/update_questions')
def update_questions():
    print('*' * 40)
    print ('update_questions')
    choice = bottle.request.forms.get('choice')
    print('choice:', choice)

    section = bottle.request.forms.get('section')
    print('#section~', section)
    section = int(section)
    # if no question location is chosen add the question to the top of the list

    question = (section * 1000) + 1
    question = bottle.request.forms.get('question')

    print('question:', question)

    questions = database.get_questions(section)
    print(questions)

            # print('cursor',cursor[0])
    query_string = 'form_name_'
    read_in_dict = readin(questions, query_string)

    if choice == 'remove':

        section = remove_question(read_in_dict, section)
    elif choice == 'edit':
        print('edit')

        query_string = 'quest_edit_'
        read_in_dict = readin(questions, query_string)
        print('read_in', read_in_dict)
        edit_questions(read_in_dict, section, questions)

    elif choice == 'add':
        print('add********************************************************')
        new_question = bottle.request.forms.get('new_question')
        print('new question:', new_question)
        tags = bottle.request.forms.get('tags')
        print('tags:', tags)

        query_string = 'form_name_'
        read_in_dict = readin(questions, query_string)

        section, tag_loc = add_question(new_question, read_in_dict, section)
        if tags != None:
            pass
            print('tagloc', tag_loc)
            add_question_tag(tags, tag_loc)

    print('********************************************************')

    # section =1
    print('!section:', section)
    cursor = database.get_questions(section)
    print ('!cursor:', cursor)

    return bottle.template('questions_edit', cursor=cursor, section=section)


def edit_questions(read_in_dict, section, questions):
    print('   ', read_in_dict, section, questions)

    for key in read_in_dict:
        key = int(key)
        question_no = (int(section) * 1000) + key
        # print(question_no)
        # print('|!!!!!!!!!!!!', read_in_dict[key], questions[key -1])
        # print('|!!!!!!!!!!!!')
        if read_in_dict[key] != questions[key - 1]:
            database.edit_question_by_number(question_no, read_in_dict[key])


def edit_sections(read_in_dict, sections):
    print('   ', read_in_dict, '   ', sections)
    for key in read_in_dict:
        key = int(key)

        # print('|!!!!!!!!!!!!', read_in_dict[key], '  ::  ', sections[key -1])
        # print('|!!!!!!!!!!!!')
        if read_in_dict[key] != sections[key - 1]:
            print('in loop')
            database.edit_section_by_number(key, read_in_dict[key])
        # get the new sections
    sections = database.get_sections()
    return sections


def remove_question(dict1, section):
    print('remove')
    print('cordiantes', dict1, section)

    for key, value in dict1.items():
        section = int(section)
        print(key, ' : ', value)
        if dict1[key] == 'on':
            position = (section * 1000) + key
            # print(position)
            database.remove_question(position)
            print('removedgui')

            # print ('questions:',questions)

    return  section


def add_section(new_section_name, location):
    print(location)
    database.add_section(new_section_name, location)
    sections = database.get_sections()
    return sections


def add_question(new_question, dict, section):
    print('add---------')
    section = int(section)

    print('dict', dict)
    # default location is
    location = int(section) * 1000 + 1
    location = database.find_last_reference_no('question', location)
    # add a new question after the last by incrementing the location
    location = location + 1
    print ('-loc', location)

    for key, value in dict.items():
        print (key)
        check = False
        if dict[key] == 'on':
            check = True
            location = int(section) * 1000 + int(key)
            print('--location --is', location)
    # if no position to add is chosen it goes first
    if check == False:
        location = int(section) * 1000 + 1
#    if location==None:
#            pass
#            location = int(section) * 1000 + 1
#            print ('loc-',location)

    print('--location --is', location)
    database.add_question(new_question, location)

#    questions = database.get_questions(section)
#    print('questions---',questions)

    return  section, location


def remove_section_tag():

    section, quest_no, tag, tag_no = get_info_from_view()

    quest_no = tag_no[0]
    print('$$$$$$$$$$$$', quest_no)
    tag = tag_no[1]
    print('$$$$$$$$$$$$', tag)

    database.remove_section_tag(quest_no, tag)
    print('_-___--')
    tags = database.get_sections_and_tags()
    return section, tags


def remove_question_tag():

    section, quest_no, tag, tag_no = get_info_from_view()

    quest_no = tag_no[0]
    print('$$$$$$$$$$$$', quest_no)
    tag = tag_no[1]
    print('$$$$$$$$$$$$', tag)

    database.remove_question_tag(quest_no, tag)
    tags = get_question_tags(section)
    return section, tags


def get_info_from_view():
    print('_________________________________________________________')
    section = bottle.request.forms.get('section')
    print('section#', section)
    if isinstance(section, str):
        # print('ssssssssss')
        section = int(section)
    quest_no = bottle.request.forms.get('quest_no')
    if isinstance(quest_no, str):
        # print('iiiiiiii')
        quest_no = int(quest_no)
    # print('quest-no#', quest_no )
    tag = bottle.request.forms.get('tags')
    print('tag#', tag)
    tag_no = bottle.request.forms.get('tag_no')
    print('tag_no#1--', tag_no)
    if isinstance(tag_no, str):
        print('eval')
        tag_no = ast.literal_eval(tag_no)
    print('tag_no#--', tag_no)

    print(quest_no, tag_no, '-----:-----', tag)
    print('_________________________________________________________')
    return section, quest_no, tag, tag_no


def add_section_tag():

    section, quest_no, tag, tag_no = get_info_from_view()

    form = bottle.request.forms.get('form_name')
    print('form', form)
    form = int(form)
    print(form)
    print(section, quest_no, tag, tag_no, '==')
    tag = bottle.request.forms.get('tags')
    print(tag)

    database.add_section_tag(form, tag)

    section_tag = get_section_tags(form)
    print('qtag-:', section_tag)

    return section_tag, form


def add_question_tag():

    section, quest_no, tag, tag_no = get_info_from_view()

    database.add_question_tag(quest_no, tag)

    question_tag = get_question_tags(section)
    print('qtag-:', question_tag)
    return question_tag, section


def get_question_tags(section_no): 
    question_tag = database.get_question_tags(section_no)
    print('________', question_tag)

    return question_tag


def get_section_tags(section_no):
    print(section_no)
    section_tag = database.get_section_tags(section_no)
    print(section_tag)
    return  section_tag


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8083)
