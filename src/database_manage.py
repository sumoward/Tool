"""
class to interact with mongo
This calls the template created by master template generator class

TODO write testing suite
"""

import pymongo
import csv


class Database_manage_recap:

    def dbconnection(self, username):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.db = self.connection.recap
        self.template = self.db.questionaire_master_template
        self.store = self.db[username]
        #print('end of connection method',self.store)
        #print(type(self.store))
        print('connection made')
        return self.store

    def copy_template(self):
        self.store.drop()
        cursor = self.template.find()
        for cur in cursor:
            temp = cur
            self.store.insert(cur)
        self.store.ensure_index('sections.section')
        print('copied template over')
        return temp

    def get_sections_and_tags(self):
        pipeline = [{'$project':{'_id':0, 'section':'$sections.section',
         'section_string':'$sections.section_string',
         'section_tag':'$sections.section_tag'}}, {'$sort':{'section': 1}}]
        cursor = self.store.aggregate(pipeline)
        cursor = cursor['result']
        return cursor

    def get_sections(self):
        print('getting sections')
        # dict1 = {}
        list1 = []

        pipeline = [{'$project':{'_id':0,
                 'sections.section':'$sections.section',
             'section_string':'$sections.section_string'}},
             {'$sort':{'sections.section': 1}}]
        cursor = self.store.aggregate(pipeline)
        cursor = cursor['result']
        for  res in cursor:
            list1.append(res['section_string'])

        return list1

    def get_section_no(self, location):
        location = int(location)
        print('this is question:', location)
        pipeline = [{'$unwind':'$sections.questions'},
                     {'$match':{'sections.questions.question':location}},
                      {'$project':{'_id':0, 'sections.section':1}}]
        section_no = self.store.aggregate(pipeline)
        section_no = section_no['result'][0]['sections']['section']
        return section_no

    def get_questions(self, section_no):

        section_no = int(section_no)
        # sort the questions so they remain in order
        pipeline = [{'$match':{'sections.section':section_no}},
         {'$unwind':'$sections.questions'}, {'$project':{'_id':0,
         'quest_no':'$sections.questions.question',
         'quest':'$sections.questions.question_string'}},
             {'$sort':{'quest_no':1}}]

        quest = self.store.aggregate(pipeline)
        print('quest--', quest)
        question_list = []
        for ques in quest['result']:
            ques = ques['quest']
            question_list.append(ques)

        return question_list

    def get_question_no(self, quest):
        pipeline = [{'$unwind':'$sections'}, {'$unwind':'$sections.questions'},
             {'$match':{'sections.questions.question_string':quest}}]
        quest = self.store.aggregate(pipeline)
        quest_no = quest['result'][0]['sections']['questions']['question']
        return quest_no

    def edit_question(self, question_string, new_question):
        self.store.update({'questions.question_string': question_string},
         {'$set': {'questions.$.question_string': new_question}})

    def edit_question_by_number(self, question_no, new_question):
        question_no = int(question_no)
        self.store.update({'sections.questions.question': question_no},
     {'$set': {'sections.questions.$.question_string': new_question}})

    def edit_section_by_number(self, section_no, new_section_string):
        print('edit section by number')
        section_no = int(section_no)
        self.store.update({'sections.section': section_no},
         {'$set': {'sections.section_string': new_section_string}})

    def add_section(self, new_section_name, location):
        self.increment_position_numbers(location, 'section')
        account_name = self.get_account_name()
        question_no = location * 1000 + 1
        first_question = {'question': question_no,
         'question_string': None, 'question_tag': [], 'answer': None}

        self.store.insert({'sections': {'section': location,
             'section_string': new_section_name,
              'section_tag': [], 'questions': [],
             'account_name': account_name}})
        # add a null question
        self.store.update({'sections.section': location},
         {'$push': {'sections.questions': first_question}})

    def add_question(self, new_question_string, location):
        section_no = self.get_section_no(location)
        self.increment_position_numbers(location, 'question')
        self.store.update({'sections.section': section_no},
     {'$push': {'sections.questions': {'question': location,
     'question_string': new_question_string,
      'question_tags': [], 'answer': None}}})

    def increment_position_numbers(self, position, type1):
        # increment when a question has been added
        if type1 == 'question':
            highest = self.find_last_reference_no(type, position)
            while highest >= position:
                    # print('highest:',highest)
                    self.store.update({'sections.questions.question': highest},
                     {'$inc': {'sections.questions.$.question': 1}})
                    highest = highest - 1
        # increment when a section has been added
        elif type1 == 'section':
            highest = self.find_last_reference_no(type, position)

            while position <= highest:
                self.store.update({'sections.section': highest},
                 {'$inc': {'sections.section': 1}})
                new_section = highest
                self.increment_all_questions_in_section(new_section, type1)
                highest = highest - 1

    def increment_all_questions_in_section(self, position, type1):
        start = position * 1000 + 1
        finish = self.find_last_reference_no('question', start)
        finish = finish + 1
        for sqq in range(start, finish):
            self.store.update({'sections.questions.question': sqq},
             {'$inc': {'sections.questions.$.question': 1000}})

    def find_last_reference_no(self, type1, position):
        account_name = self.get_account_name()
        if type1 == 'question':
            pipeline = [{'$match':{'sections.questions.question':position}},
         {'$unwind':'$sections.questions'},
     {'$group':{'_id':'$sections.section',
     'highest':{'$max':'$sections.questions.question'}}},
     {'$sort':{'highest':-1}}, {'$limit':1}]

        # get the number of the last question
        elif type1 == 'section':

            pipeline = [{'$match':{'sections.account_name':account_name}},
                        {'$group':{'_id':'$sections.section',
                                   'highest':{'$max':'$sections.section'}}},
                     {'$sort': {'highest':-1}}, {'$limit':1}]

        ans = self.store.aggregate(pipeline)
        print('ans1', ans)
        if ans['result'] == []:
            return position
        else:
            ans = ans['result'][0]['highest']
            print('ans', ans)
            return ans

    def get_section_from_question(self, position):
        return int(str(position)[:-3])

    def lowest_first_reference_no(self, type1, position):
        account_name = self.get_account_name()
        if type1 == 'question':
            position = self.get_section_from_question(position)
            print('qp', position)

            pipeline = [{'$match':{'sections.section':position}},
             {'$unwind': '$sections.questions'},
              {'$group':{'_id':'$sections.questions.question',
         'lowest':{'$min':'$sections.questions.question'}}},
                 {'$sort':{'lowest':1}},
             {'$limit':1}]

        elif type1 == 'section':

            pipeline = [{'$match':{'sections.account_name':account_name}},
         {'$group':{'_id':'$sections.section',
         'lowest':{'$min':'$sections.section'}}},
     {'$sort':{'lowest':1}}, {'$limit':1}]

        ans = self.store.aggregate(pipeline)
        ans = ans['result'][0]['_id']
        return ans

    def remove_section(self, position):
        self.store.remove({'sections.section': position})

    def reorder_position_numbers(self, type1, position):
        highest = self.find_last_reference_no(type, position)
        holder = position
        for x in range(position - 1, highest):
            print(position, 'position becomes', x)
            self.store.update({'sections.section': position},
             {'$set': {'sections.section': x}})

            position = position + 1
        for x in range(holder, highest):
            self.reorder_question_numbers(x)

    def reorder_question_numbers(self, position):
        pipeline = [{'$match':{'sections.section':position}},
         {'$unwind':'$sections.questions'},
         {'$group':{'_id':'$sections.section',
         'highest':{'$max':'$sections.questions.question'}}}]
        highest = self.store.aggregate(pipeline)
        highest = highest['result'][0]['highest']
        pipeline = [{'$match':{'sections.section':position}},
         {'$unwind':'$sections.questions'},
         {'$group':{'_id':'$sections.section',
         'lowest':{'$min':'$sections.questions.question'}}}]
        lowest = self.store.aggregate(pipeline)
        lowest = lowest['result'][0]['lowest']
        # create the modifier we use to make the questions reflect the section
        mod = self.get_section_from_question(lowest)
        mod = mod * 1000
        end = highest - mod
        mod = (mod) - 1000
        for x in range(end):
            mod = mod + 1
            self.store.update({'sections.questions.question': lowest},
             {'$set': {'sections.questions.$.question': mod}})
            lowest = lowest + 1

    def remove_question(self, position):
        # check what the highest and lowest referecesa re before deleting
        lowest = self.lowest_first_reference_no('question', position)
        highest = self.find_last_reference_no('question', position)
        # remove the question document
        self.store.update({'sections.questions.question': position},
         {'$pull': {'sections.questions': {'question': position}}})
        # decrement the numbers
        self.decrement_questions(position, lowest, highest)

    def decrement_section(self, position):
        position = position + 1
        highest = self.find_last_reference_no('section', position)
        print('highest:', highest)

    def decrement_questions(self, position, lowest, highest):
        section_no = self.get_section_from_question(position)
        counter = section_no * 1000 + 1
        if position == highest:
            return highest
        if position != highest:
            position = position + 1
            while position <= highest:
                self.store.update({'sections.questions.question': position},
             {'$inc': {'sections.questions.$.question': -1}})
                position = position + 1
        return position

    def export_csv(self):
        csvfilename = 'saved version of the recap database'
        result_writer = csv.writer(open(csvfilename,
         'w'), delimiter=',', lineterminator='\n')

        # get highest section number
        highest = self.find_last_reference_no(type, position)
        for x in range(highest + 1):
            results = self.store.find({'sections.section': x})
            for result in results:
                input1 = result['sections']['section']
                input2 = result['sections']['section_string']
                input3 = result['sections']['questions']
                result_writer.writerow([input1, input2])
                for each in input3:
                    result_writer.writerow([each['question'],
                             each['question_string']])
                result_writer.writerow([])

    def update_account_name(self, old_account_name, new_account_name):
        self.store.update({'sections.account_name': old_account_name},
         {'$set': {'sections.account_name': new_account_name}}, multi=True)

    def get_account_name(self):
        account = self.store.find_one()
        account = account['sections']['account_name']
        return account

    def add_section_tag(self, location, tag_name):
        self.store.update({'sections.section': location},
         {'$push': {'sections.section_tag': tag_name}})

    def remove_section_tag(self, location, tag_name):
        self.store.update({'sections.section': location},
             {'$pull': {'sections.section_tag': tag_name}})

    def add_question_tag(self, location, tag_name):
        self.store.update({'sections.questions.question': location},
         {'$push': {'sections.questions.$.question_tag': tag_name}})

    def remove_question_tag(self, location, tag_name):
        self.store.update({'sections.questions.question': location},
         {'$pull': {'sections.questions.$.question_tag': tag_name}})

    def get_section_tags(self, section_no):
        section_no = int(section_no)
        # sort the questions so they remain in order
        pipeline = [{'$match':{'sections.section':section_no}},
                     {'$project':{'_id': 0,
                 'tags': '$sections.section_tag'}}]

        sect = self.store.aggregate(pipeline)
        sect = sect['result'][0]['tags']
        return sect

    def get_question_tags(self, section_no):
        section_no = int(section_no)
        # sort the questions so they remain in order
        pipeline = [{'$match':{'sections.section':section_no}},
         {'$unwind':'$sections.questions'},
          {'$project':{'_id':0, 'tags':'$sections.questions.question_tag',
                     'quest_no':'$sections.questions.question',
         'quest':'$sections.questions.question_string'}},
             {'$sort':{'quest_no':1}}]

        quest = self.store.aggregate(pipeline)
        quest = quest['result']
        return quest

    def create_interface_dict(self, page, customer_name):
        print ('in data manage',customer_name)
        if page == 'sales':
            modifier = {'sections.section': {'$lte': 12}}
        elif page == 'scoping':
            modifier = {'sections.section': {'$gt': 12,'$lt': 45}}
        elif page == 'prof':
            print('prof')
            modifier = {'sections.section': {'$gte': 45}}
        else:
            modifier = {'sections.section': {'$gte': 1}}

        pipeline1 = [{'$match':modifier},
                     {'$project':{'_id':0,
                         'section_no':'$sections.section',
         'section_name':'$sections.section_string',
         'intro':'$sections.intro',
         'free_text':'$sections.free_text'}},
                     {'$sort':{'section_no':1}}]

        pipeline2 = [{'$match':modifier},
                     {'$unwind':'$sections.questions'}, {'$project':{'_id':0,
                 'section_no': '$sections.section',
                  'quest_no':'$sections.questions.question',
         'quest':'$sections.questions.question_string',
          'answer':'$sections.questions.answer',
          'subhead':'$sections.questions.subhead'}},
         {'$sort':{'quest_no':1, 'section_no':1}}]

        #check if the collections exits
        self.check_create_db(customer_name)
        section_interface_dict = self.store.aggregate(pipeline1)
        section_interface_dict = section_interface_dict['result']
        question_interface_dict = self.store.aggregate(pipeline2)
        question_interface_dict = question_interface_dict['result']

        return section_interface_dict, question_interface_dict

    def check_create_db(self, customer_name):
        #print('un',customer_name)
        #check if the collection exists
        #print('-----------')
        db = self.dbconnection(customer_name)
        #print('db names inside:', self.connection.database_names())
        collections = self.connection['recap'].collection_names()
        #print('collections', collections)
        #if collection exists return if not create one from the template
        if customer_name in collections:
            return customer_name
        return self.copy_template()

    def count_questions(self, section_no):
        pipeline = [{'$match':{'sections.section':section_no}},
             {'$unwind':'$sections.questions'},
             {'$project':{'_id':0, 'no':'$sections.questions.question'}},
     {'$group':{'_id':'$sections.questions.question', 'count':{'$sum':1}}}]

        count = self.store.aggregate(pipeline)
        count = count['result'][0]['count']
        return count

    def save_answer(self, question_no, answer,customer_name):
        print(customer_name)
        self.dbconnection(customer_name)
        print(self.store)
        self.store.update({'sections.questions.question': question_no},
         {'$set': {'sections.questions.$.answer': answer}})

    def create_new_tag(self, new_tag_name):
        pipeline = [{'$match':{'container_name':'storage_array_for_tags'}}]
        check = self.store.aggregate(pipeline)
        if check['result'] == []:
            self.store.insert({'container_name': 'storage_array_for_tags',
                     'tag': []})
        else:
            self.store.update({'container_name': 'storage_array_for_tags'},
                     {'$push': {'tag': new_tag_name}})

        tag_array = self.get_list_tag_names()
        return tag_array

    def remove_tag_name_array(self, old_tag_name):
        self.store.update({'container_name': 'storage_array_for_tags'},
         {'$pull': {'tag': old_tag_name}})
        tag_array = self.get_list_tag_names()
        return tag_array

    def get_list_tag_names(self):
        pipeline = [{'$match':{'container_name':'storage_array_for_tags'}}]
        result = self.store.aggregate(pipeline)
        if result['result'] == []:
            result = []
            return result
        result = result['result'][0]['tag']
        return result

    def add_free_text(self, section_no, free_text, customer_name):
        """
        to remove free text just set free_text to None
        """
        self.dbconnection(customer_name)
        self.store.update({'sections.section': section_no},
                     {'$set': {'sections.free_text':  free_text}})

    def get_free_text(self, section_no):
        pipeline = [{'$match':{'sections.section':section_no}},
          {'$project':{'_id':1, 'sections.free_text':'$sections.free_text'}}]
        quest = self.store.aggregate(pipeline)
        try:
            quest = quest['result'][0]['sections']['free_text']
        except:
            print('exception')
            quest = None
        return quest

    def add_subhead(self, question_no, subhead_text):
        self.store.update({'sections.questions.question': question_no},
         {'$set': {'sections.questions.$.subhead':  subhead_text}})

    def get_subhead(self, question_no):
        pipeline = [{'$unwind': "$sections.questions"},
            {'$match':{'sections.questions.question':question_no}},
        {'$project':{'_id':0,
         'sections.questions.subhead':'$sections.questions.subhead'}}]
        subhead = self.store.aggregate(pipeline)
        subhead = subhead['result'][0]['sections']['questions']['subhead']
        return subhead

    def phase1(self):
        pipeline = [{'$unwind':'$sections.questions'},
                    {'$match':{'sections.section':{'$lte':3}}},
                    {'$project':{'_id':0,
                 'section_no': '$sections.section',
                  'quest_no':'$sections.questions.question',
         'quest':'$sections.questions.question_string',
          'answer':'$sections.questions.answer'}},
                     {'$sort':{'section_no':1}}]
        phase1 = self.store.aggregate(pipeline)
        #print (phase1)
        phase1 = phase1['result']
        return phase1

if __name__ == "__main__":

########################################################
    tester1 = Database_manage_recap()
    username ="aab"
    tester1.dbconnection(username)
    #print("___________________________________________________________")
    tester1.copy_template()
    #tester1.get_sections()
    section_no = 2
    #print("____________________________________________________")
    tester1.get_questions(section_no)
    quest = 'What is the current total number of warehouses floor operatives?'
    # tester1.get_question_no(quest)
    new_question = 'test7'
    question_string = 'What is the  floor operatives?'
    # tester1.edit_question(question_string,new_question)

    account_name = 'principle1'

    position = 1
    type1 = 'section'
    # tester1.increment_position_numbers(position,type1)
# tester1.find_last_reference_no(type, 1)
#    new_question_string = 'new question new question new question'
#    location = 2002
#    tester1.add_question(new_question_string, location)
#    new_section_name = 'Brians new section'
#    location = 2
#    tester1.add_section(new_section_name, location)
#    new_question_string = 'blah blah blah blah'
#    location = 2001
#    tester1.add_question(new_question_string, location)
#    location = 3002
#    #tester1.remove_question(location)
    section = 1
    #print('______________________________________________')
    # tester1.remove_section(section)
    # tester1.add_section_tag(2, 'ROI')
#    #tester1.remove_section_tag(2, 'ROI')
#
# tester1.add_question_tag(1001, 'ROI1')
#    tester1.add_question_tag(1002, 'ROI2')
#    tester1.add_question_tag(1003, 'ROI3')
#    #tester1.remove_question_tag(2002, 'ROI2')
#    tester1.export_csv()
#    tester1.get_question_tags(section)
#   tester1.count_questions(3)
    # #tester1.save_answer(1001, 'sheep')
    # tester1.create_interface_dict()

    # lowest = tester1.lowest_first_reference_no('question', 3002)
    # highest = tester1.find_last_reference_no('question', 3002)
    # tester1.remove_question(3002)

# tester1.decrement_questions(3002, lowest, highest)
    #tester1.add_section_tag(1, 'tag_name')
    #tester1.get_section_tags(1)
    #print('_________interface______________')
# free_text = 'test text for free text'
# tester1.add_free_text(1, None)
    #tester1.get_free_text(1)
    #subhead_text = 'subhead this is a test subhead'
    #subhead_text2 = 's2222222222'

    #tester1.add_subhead(1001, subhead_text)
    #tester1.add_subhead(1003, subhead_text2)
    #tester1.get_subhead(1001)
    tester1.phase1()
