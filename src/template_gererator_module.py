"""
this class takes the excel spreadsheet with the recap
questions and creates database schema
"""

import pymongo
import pickle


class Import:

    def __init__(self):
        self.file = 'final_questions.csv'
        #self.file = 'complex_short.csv'
        #self.file = 'complex2.csv'
        self.counter1 = 1
        self.counter2 = 1
        self.account = {'account_name': None}
        self.subhead = None
        self.intro = None

    def readin(self):
        # print("test1")
        self.holder = open(self.file, 'r')
        # print(self.holder)
        return self.holder

    def start(self):
        #print('start')
        self.connect_to_mongo()

    def parse_entry(self, line):
        # print('parse\n')
        line = line.strip()
        # print('line')
        line = line.replace('"', '')
        line = line.replace(',', ' ')
        #print(line)
        return line

    def connect_to_mongo(self):

        connection = pymongo.MongoClient("localhost", 27017)
        db = connection.recap
        self.customer = db.template1
        # drop the old template
        self.customer.drop()

    def string_persist(self):

        template = self.customer.find()

        for cur in template:
            #print (cur)
            pickle.dump(cur, open("save.p", "wb"))  # @UndefinedVariable

        # function to print out result
    def writeout(self):
        self.document = self.readin()
        # print(self.document)
        for entry in self.document:
            # parse the entry
            entry = self.parse_entry(entry)
            #print(entry)
            # self.customer.insert(self.account)
            # check to see if it is used to generate the variable name
            if 'section' in entry:
                self.customer.insert({'sections': {'section': self.counter1,
              'section_string': entry,
              'intro': self.intro,
                 'section_tag': [], 'questions': [],
                  'account_name': None, 'free_text': None}})
            elif '*%$subhead$%*' in entry:
                #print('**----------------------------------**')
                self.subhead = entry[14:]

            elif '*%$introduction$%*' in entry:
                print('***----------------------------------**')
                self.customer.update({'sections.section': self.counter1},
                                     {'$set': {'sections.intro': entry[19:]}})
                print('-------------------intro here', entry[19:])

            # the empty line in the spreadsheet
            elif  '*%$break&%*' in entry:
                #print('the counter is at', self.counter1)
                self.counter1 = self.counter1 + 1
                print('the counter is at', self.counter1)
                self.counter2 = 1
            # input the questions from the spreadsheet
            else:
                pass
                question_refernce_no = ((self.counter1 * 1000) + self.counter2)
                # print(question_refernce_no)'
                # add in the questions we wish to add to the section
                questionaire = {'question': question_refernce_no,
                 'question_string': entry.strip(),
                  'question_tag': [], 'answer': None, 'subhead': self.subhead}
                self.customer.update({'sections.section': self.counter1},
{'$push': {'sections.questions': questionaire}})
                self.counter2 = self.counter2 + 1
                #print(questionaire)
        # persist the template
        self.string_persist()

if __name__ == "__main__":

############################################################################
    tester1 = Import()
    # print("________________________________________________________")
    tester1.start()
    # print("_______________________________________________________")
    tester1.writeout()
