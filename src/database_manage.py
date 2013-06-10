"""
class to interact with mongo
"""
import pymongo
import csv


class Database_manage_recap:

    def __init__(self):
        pass
        # print('instaate')

        # self.template={}
        # self.store ={}

    def connection(self):
        pass
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection.recap
        self.template = db.template1
        self.store = db.template4
        # print('connected to mongo')

    def copy_template(self):
        pass
        # print('temp')
        self.store.drop()
        cursor = self.template.find()
        for cur in cursor:
            # print(cur)
            temp = cur
            self.store.insert(cur)
        print('copied template over')
        # 'create a store for tags
        return temp

    def get_sections_and_tags(self):
        pass
        pipeline = [{'$project':{'_id':0, 'section':'$sections.section',
         'section_string':'$sections.section_string',
         'section_tag':'$sections.section_tag'}}, {'$sort':{'section': 1}}]
        cursor = self.store.aggregate(pipeline)
        print(cursor)
        cursor = cursor['result']

        print(cursor)
        return cursor

    def get_sections(self):
        pass
        print('getting sections')
        # dict1 = {}
        list1 = []

        # {'$project':{'_id':0, 'sections':1}},
        # {'$unwind':'$sections'},
        # {'$group':{'_id':'$sections'}}
        # {'$group':{'_id':'$sections','num sections':{'$sum':1}}}

        pipeline = [{'$project':{'_id':0,
                 'sections.section':'$sections.section',
             'section_string':'$sections.section_string'}},
             {'$sort':{'sections.section': 1}}]
        cursor = self.store.aggregate(pipeline)
        # print(cursor)
        cursor = cursor['result']

        print(cursor)

        for  res in cursor:

            list1.append(res['section_string'])

        return list1

#        for cur in cursor:
#           print (cur[1])

    def get_section_no(self, location):
        # section = 'section 1 Staff Breakdown'
        # section = section[2:-2].strip()
        location = int(location)
        print('this is question:', location)
        # optain the setcion number
        # print (section)

        pipeline = [{'$unwind':'$sections.questions'},
                     {'$match':{'sections.questions.question':location}},
                      {'$project':{'_id':0, 'sections.section':1}}]
        section_no = self.store.aggregate(pipeline)
        print(section_no)
        section_no = section_no['result'][0]['sections']['section']
        print(section_no)
        return section_no

    def get_questions(self, section_no):
        # get the number of the section
        # print('section:',section)
        # section_no =self.get_section_no(section)
        # section_no = section_no *1000
        # print('section_no:',section_no)
        # regex_patern = '^' + str(section_no) +'[0-9]{3}$'
        # obtain the questions for that section

        # get the highests question no
        # type1 = 'question'
        # highest = self.find_last_reference_no(type )
        # print('high', highest)
                # section_no =section_no
        # match = {'section': section_no}
        print('   ', section_no)
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
            # print(ques)
            ques = ques['quest']
            # print(ques)
            question_list.append(ques)
        print('question_list:', question_list)

        return question_list

    def get_question_no(self, quest):

        pipeline = [{'$unwind':'$sections'}, {'$unwind':'$sections.questions'},
             {'$match':{'sections.questions.question_string':quest}}]
        quest = self.store.aggregate(pipeline)
        # print('quest :',quest)
        quest_no = quest['result'][0]['sections']['questions']['question']
        # print('quest:',quest_no)
        return quest_no

    def edit_question(self, question_string, new_question):

        self.store.update({'questions.question_string': question_string},
         {'$set': {'questions.$.question_string': new_question}})
        # print('updated questions')

    def edit_question_by_number(self, question_no, new_question):
        print('edit by no__________', question_no, new_question)

        question_no = int(question_no)
        self.store.update({'sections.questions.question': question_no},
     {'$set': {'sections.questions.$.question_string': new_question}})

    def edit_section_by_number(self, section_no, new_section_string):
        print('edit section by number')
        section_no = int(section_no)
        self.store.update({'sections.section': section_no},
         {'$set': {'sections.section_string': new_section_string}})

    def add_section(self, new_section_name, location):
        # new_section_name = 'This is our new test section'

        self.increment_position_numbers(location, 'section')
        account_name = self.get_account_name()
        # print(account_name)
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

        # print('section added')

    def add_question(self, new_question_string, location):

        section_no = self.get_section_no(location)
        print(section_no, 'sn')

        self.increment_position_numbers(location, 'question')

        self.store.update({'sections.section': section_no},
     {'$push': {'sections.questions': {'question': location,
     'question_string': new_question_string,
      'question_tags': [], 'answer': None}}})

    def increment_position_numbers(self, position, type1):

        # increment when a question has been added
        if type1 == 'question':
            highest = self.find_last_reference_no(type, position)
            print(highest, '..............')
            # print('postion:',position)
            while highest >= position:
                    # print('highest:',highest)
                    self.store.update({'sections.questions.question': highest},
                     {'$inc': {'sections.questions.$.question': 1}})
                    highest = highest - 1

        # increment when a section has been added
        elif type1 == 'section':
# print('______________')
            # print(type)
            # print(position)
            highest = self.find_last_reference_no(type, position)

            while position <= highest:
                # print('x',x)
                # print('highest',highest)
                self.store.update({'sections.section': highest},
                 {'$inc': {'sections.section': 1}})
                new_section = highest
                self.increment_all_questions_in_section(new_section, type1)

                highest = highest - 1

    def increment_all_questions_in_section(self, position, type1):
        pass
        # print('all question all in section________________________________')
        start = position * 1000 + 1
        # print('s',start)
        # print('position:',position)
        finish = self.find_last_reference_no('question', start)
        finish = finish + 1

        for sqq in range(start, finish):
            # print('sqq',sqq)
            self.store.update({'sections.questions.question': sqq},
             {'$inc': {'sections.questions.$.question': 1000}})

    def find_last_reference_no(self, type1, position):
        # print('tp',type, position)
        account_name = self.get_account_name()

        if type1 == 'question':
            print('p', position)
            # loc= str(position)
            pipeline = [{'$match':{'sections.questions.question':position}},
         {'$unwind':'$sections.questions'},
     {'$group':{'_id':'$sections.section',
     'highest':{'$max':'$sections.questions.question'}}},
     {'$sort':{'highest':-1}}, {'$limit':1}]

        # get the number of the last question
        elif type1 == 'section':

            # print(account_name)
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
        print(position)
        return int(str(position)[:-3])

    def lowest_first_reference_no(self, type1, position):
        pass
        print('low', type1)
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

            # print('ac',account_name)
            pipeline = [{'$match':{'sections.account_name':account_name}},
         {'$group':{'_id':'$sections.section',
         'lowest':{'$min':'$sections.section'}}},
     {'$sort':{'lowest':1}}, {'$limit':1}]

        ans = self.store.aggregate(pipeline)
        print('ans', ans)
        ans = ans['result'][0]['_id']
        print('ans', ans)
        return ans

    def remove_section(self, position):
        pass
        # remove the section document
        self.store.remove({'sections.section': position})
        # decrement the sections
        # self.decrement_section(position)
        # self.reorder_position_numbers('section', position)

    def reorder_position_numbers(self, type1, position):
        highest = self.find_last_reference_no(type, position)
        # print ('H',highest)
        # lowest = self.lowest_first_reference_no(type, position)
        # print ('L',lowest)
        # highest = highest + 1
        holder = position
        for x in range(position - 1, highest):
            # print(x)
            print(position, 'position becomes', x)
            self.store.update({'sections.section': position},
             {'$set': {'sections.section': x}})
            # quest_no = x

            position = position + 1
        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for x in range(holder, highest):
            # print('x:',x)
            self.reorder_question_numbers(x)

    def reorder_question_numbers(self, position):
        print ('Pq___________________________________', position)
        # highest = self.find_last_reference_no('question', position)
        pipeline = [{'$match':{'sections.section':position}},
         {'$unwind':'$sections.questions'},
         {'$group':{'_id':'$sections.section',
         'highest':{'$max':'$sections.questions.question'}}}]
        highest = self.store.aggregate(pipeline)
        # print ('Hq',highest)
        highest = highest['result'][0]['highest']
        # print ('Hq',highest)

        pipeline = [{'$match':{'sections.section':position}},
         {'$unwind':'$sections.questions'},
         {'$group':{'_id':'$sections.section',
         'lowest':{'$min':'$sections.questions.question'}}}]
        lowest = self.store.aggregate(pipeline)
        lowest = lowest['result'][0]['lowest']
        # print ('Lq',lowest)
        # create the modifier we use to make the questions reflect the section
        mod = self.get_section_from_question(lowest)
        print ('me', mod)
        mod = mod * 1000
        # end = highest - mod
        end = highest - mod
        print ('end', end)
        mod = (mod) - 1000

        print ('mod', mod)
        for x in range(end):
            print(x)
            print(mod, 'm')
            mod = mod + 1
            # print(mod,'m')
            print(lowest, 'lowest becomes', mod)

            self.store.update({'sections.questions.question': lowest},
             {'$set': {'sections.questions.$.question': mod}})
            lowest = lowest + 1

    def remove_question(self, position):

        print('position is', position)
        # check what the highest and lowest referecesa re before deleting
        lowest = self.lowest_first_reference_no('question', position)
        highest = self.find_last_reference_no('question', position)
        # remove the question document
        self.store.update({'sections.questions.question': position},
         {'$pull': {'sections.questions': {'question': position}}})
        # decrement the numbers
        self.decrement_questions(position, lowest, highest)

    def decrement_section(self, position):
        pass
        position = position + 1
        # print(position)
        highest = self.find_last_reference_no('section', position)
        print('highest:', highest)

    def decrement_questions(self, position, lowest, highest):
        # pass
        # get the next position
        print('____________', position, lowest, highest)

        section_no = self.get_section_from_question(position)
        counter = section_no * 1000 + 1
        print('counter', counter)

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
        pass
        print('write out')
        csvfilename = 'saved version of the recap database'
        result_writer = csv.writer(open(csvfilename,
         'w'), delimiter=',', lineterminator='\n')

        # get highest section number
        highest = self.find_last_reference_no(type, position)
        print(highest)

        for x in range(highest + 1):
            results = self.store.find({'sections.section': x})
            print(results)
            for result in results:
                print(result)
                input1 = result['sections']['section']
                input2 = result['sections']['section_string']
                input3 = result['sections']['questions']

                print(input1)
                print(input2)
                print(input3)
                result_writer.writerow([input1, input2])
                for each in input3:
                    result_writer.writerow([each['question'],
                             each['question_string']])
                result_writer.writerow([])

    def update_account_name(self, old_account_name, new_account_name):
        print('new', new_account_name, 'old', old_account_name)
        self.store.update({'sections.account_name': old_account_name},
         {'$set': {'sections.account_name': new_account_name}}, multi=True)
        print('account changed')

    def get_account_name(self):

        account = self.store.find_one()
        print (account)
        account = account['sections']['account_name']

        print ('account', account)
        return account

    def add_section_tag(self, location, tag_name):
        print('tag______________', location, tag_name)
        self.store.update({'sections.section': location},
         {'$push': {'sections.section_tag': tag_name}})
        print('tag_ added')

    def remove_section_tag(self, location, tag_name):
        print('removetag______________', location, tag_name)
        self.store.update({'sections.section': location},
             {'$pull': {'sections.section_tag': tag_name}})

    def add_question_tag(self, location, tag_name):
        print('tag______________', tag_name, location)

        self.store.update({'sections.questions.question': location},
         {'$push': {'sections.questions.$.question_tag': tag_name}})

    def remove_question_tag(self, location, tag_name):
        print('removetag______________', location, tag_name)
        self.store.update({'sections.questions.question': location},
         {'$pull': {'sections.questions.$.question_tag': tag_name}})

    def get_section_tags(self, section_no):
        print('______________________________________________________________')
        print('   ', section_no)
        section_no = int(section_no)
        # sort the questions so they remain in order
        pipeline = [{'$match':{'sections.section':section_no}},
                     {'$project':{'_id': 0,
                 'tags': '$sections.section_tag'}}]

        sect = self.store.aggregate(pipeline)
        print('sect--', sect)
        sect = sect['result'][0]['tags']
        print('sect--', sect)
        return sect

    def get_question_tags(self, section_no):
        print('______________________________________________')
        print('   ', section_no)
        section_no = int(section_no)
        # sort the questions so they remain in order
        pipeline = [{'$match':{'sections.section':section_no}},
         {'$unwind':'$sections.questions'},
          {'$project':{'_id':0, 'tags':'$sections.questions.question_tag',
                     'quest_no':'$sections.questions.question',
         'quest':'$sections.questions.question_string'}},
             {'$sort':{'quest_no':1}}]

        quest = self.store.aggregate(pipeline)
        # print('quest--', quest)
        quest = quest['result']
        # print('quest--', quest)
        return quest

    def create_interface_dict(self, page):

        if page == 'sales':
            modifier = {'sections.section': {'$lte': 12}}
        elif page == 'scoping':
            modifier = {'sections.section': {'$gt': 12}}
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
        section_interface_dict = self.store.aggregate(pipeline1)
        # print(section_interface_dict)
        section_interface_dict = section_interface_dict['result']
        # print(section_interface_dict)

        question_interface_dict = self.store.aggregate(pipeline2)
        # print('q:', question_interface_dict)
        question_interface_dict = question_interface_dict['result']
        # print(question_interface_dict)

        return section_interface_dict, question_interface_dict

    def count_questions(self, section_no):
        print('s', section_no)

        pipeline = [{'$match':{'sections.section':section_no}},
             {'$unwind':'$sections.questions'},
             {'$project':{'_id':0, 'no':'$sections.questions.question'}},
     {'$group':{'_id':'$sections.questions.question', 'count':{'$sum':1}}}]

        count = self.store.aggregate(pipeline)
        print('count:', count)
        count = count['result'][0]['count']
        print('count:', count)
        return count

    def save_answer(self, question_no, answer):
        print(question_no, ' : ', answer)

        self.store.update({'sections.questions.question': question_no},
         {'$set': {'sections.questions.$.answer': answer}})
        print('updated')

    def create_new_tag(self, new_tag_name):

        print('new tag>', new_tag_name)
        pipeline = [{'$match':{'container_name':'storage_array_for_tags'}}]
        check = self.store.aggregate(pipeline)
        print(check['result'])

        if check['result'] == []:
            # print('begin')
            self.store.insert({'container_name': 'storage_array_for_tags',
                     'tag': []})
        else:
            # print('else')
            self.store.update({'container_name': 'storage_array_for_tags'},
                     {'$push': {'tag': new_tag_name}})

        tag_array = self.get_list_tag_names()
        print(tag_array, ' is returned from add')
        return tag_array

    def remove_tag_name_array(self, old_tag_name):
        self.store.update({'container_name': 'storage_array_for_tags'},
         {'$pull': {'tag': old_tag_name}})
        tag_array = self.get_list_tag_names()
        print(tag_array, ' is returned from remove')
        return tag_array

    def get_list_tag_names(self):
        # print('list tag')
        pipeline = [{'$match':{'container_name':'storage_array_for_tags'}}]
        result = self.store.aggregate(pipeline)
        # print(result)
        if result['result'] == []:
            # print('if')
            result = []
            return result
        result = result['result'][0]['tag']
        # print(result)
        return result

    def add_free_text(self, section_no, free_text):
        """
        to remove free text just set free_text to None
        """
        print('add', section_no, free_text)
        self.store.update({'sections.section': section_no},
                     {'$set': {'sections.free_text':  free_text}})

    def get_free_text(self, section_no):

        print('get free text')
        pipeline = [{'$match':{'sections.section':section_no}},
          {'$project':{'_id':1, 'sections.free_text':'$sections.free_text'}}]
        quest = self.store.aggregate(pipeline)
        print (quest)
        try:
            quest = quest['result'][0]['sections']['free_text']
        except:
            print('exception')
            quest = None

        print ('quest', quest)
        return quest

    def add_subhead(self, question_no, subhead_text):
        print(question_no, ' , ', subhead_text)
        self.store.update({'sections.questions.question': question_no},
         {'$set': {'sections.questions.$.subhead':  subhead_text}})

    def get_subhead(self, question_no):
        print('q no', question_no)
        pipeline = [{'$unwind': "$sections.questions"},
            {'$match':{'sections.questions.question':question_no}},
        {'$project':{'_id':0,
         'sections.questions.subhead':'$sections.questions.subhead'}}]
        subhead = self.store.aggregate(pipeline)
        print(subhead)
        subhead = subhead['result'][0]['sections']['questions']['subhead']
        print('sb', subhead)
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

        print ('@$$$$', phase1)
 
 
 
        return phase1

if __name__ == "__main__":

########################################################
    tester1 = Database_manage_recap()
    # print("______________________________________________________")
    tester1.connection()
    print("___________________________________________________________")
    tester1.copy_template()
    tester1.get_sections()
    section_no = 2
    print("____________________________________________________")
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
    print('______________________________________________')
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
    print('_________interface______________')
   # free_text = 'test text for free text'
   # tester1.add_free_text(1, None)
    #tester1.get_free_text(1)
    #subhead_text = 'subhead this is a test subhead'
    #subhead_text2 = 's2222222222'

    #tester1.add_subhead(1001, subhead_text)
    #tester1.add_subhead(1003, subhead_text2)
    #tester1.get_subhead(1001)
    tester1.phase1()
