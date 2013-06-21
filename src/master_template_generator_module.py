"""
this class takes the excel spreadsheet with the recap
questions and creates database schema
"""

import pymongo
import pickle


class Import:

    def __init__(self):
        self.file = 'static/documents/final_questions.csv'
        self.counter1 = 1
        self.counter2 = 1
        self.account = {'account_name': None}
        self.subhead = None
        self.intro = None

    def readin(self):
        self.holder = open(self.file, 'r')
        return self.holder

    def start(self):
        self.connect_to_mongo()

    def parse_entry(self, line):
        line = line.strip()
        line = line.replace('"', '')
        line = line.replace(',', ' ')
        return line

    def connect_to_mongo(self):

        connection = pymongo.MongoClient("localhost", 27017)
        db = connection.recap
        self.customer = db.questionaire_master_template
        self.customer.drop()

    def string_persist(self):

        template = self.customer.find()
        for cur in template:
            pickle.dump(cur, open("save.p", "wb"))  # @UndefinedVariable

        # function to print out result
    def writeout(self):
        self.document = self.readin()
        for entry in self.document:
            # parse the entry
            entry = self.parse_entry(entry)
            # check to see if it is used to generate the variable name
            if 'section' in entry:
                self.customer.insert({'sections': {'section': self.counter1,
              'section_string': entry,
              'intro': self.intro,
                 'section_tag': [], 'questions': [],
                  'account_name': None, 'free_text': None}})
            elif '*%$subhead$%*' in entry:
                self.subhead = entry[14:]
            elif '*%$introduction$%*' in entry:
                self.customer.update({'sections.section': self.counter1},
                                     {'$set': {'sections.intro': entry[19:]}})
            # the empty line in the spreadsheet
            elif  '*%$break&%*' in entry:
                self.counter1 = self.counter1 + 1
                self.counter2 = 1
            # input the questions from the spreadsheet
            else:
                pass
                question_refernce_no = ((self.counter1 * 1000) + self.counter2)
                # add in the questions we wish to add to the section
                questionaire = {'question': question_refernce_no,
                 'question_string': entry.strip(),
                  'question_tag': [], 'answer': None, 'subhead': self.subhead}
                self.customer.update({'sections.section': self.counter1},
{'$push': {'sections.questions': questionaire}})
                self.counter2 = self.counter2 + 1
        # persist the template
        self.string_persist()

if __name__ == "__main__":
    tester1 = Import() 
    tester1.start()
    tester1.writeout()
    print('completed')
