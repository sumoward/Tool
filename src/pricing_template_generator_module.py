"""
this class takes the excel spreadsheet with the pricing details
 and creates a database 'schema'
"""

import pymongo


class Price_Import:

    def readin(self):
        self.holder = open(self.file, 'r',encoding='iso-8859-1')#encoding='iso-8859-1'??
        return self.holder

    def start(self):
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection.recap
        self.pricing = db.pricing_master_template
        self.pricing.drop()
        print('Connection made')

# function to print out result
    def writeout(self, filename):
        self.file = filename
        print(filename)
        self.document = self.readin()
        print(self.document)
        counter = 1
        for entry in self.document:
            #print(entry)
            if '$%title$%' in entry:
                #print (entry)
                parse = entry[10:-2]
                #print ('parsed ', parse)
                self.pricing.insert({'section_no': counter,'section_name':parse, 'categories': [], 'section_total': 0})
                #self.pricing.update({'section_name':parse})
                #counter = counter + 1
                #self.pricing.update({'categories': []})
                #self.pricing.insert({'section_total': 0})
            elif '$%sub$%' in entry:
                #print (entry)
                self.subhead = entry[6:]
                #print ('subhead', self.subhead)
            elif '$%desc$%' in entry:
                #print (entry)
                desc = entry[9:-1]
                print(desc)
                #split the category and the list price by
                desc = desc.split(',')
                #print(desc)
                line = ({'category': desc[0],
                                   'list_price': desc[1],
                                   'quantity': 0,
                                   'sub_total':0})
                print(line)
                self.pricing.update({'section_name':parse},{'$push':{'categories':line}})
            elif '$%end$%' in entry:
                print (counter)
                counter = counter + 1

if __name__ == "__main__":
    tester1 = Price_Import()
    tester1.start()
    pricefile = 'static/pricing/pricing_testcase.csv'
    tester1.writeout(pricefile)
    print('pricing completed')
