"""
this class takes the excel spreadsheet with the pricing details
 and creates a database 'schema'
"""

import pymongo


class Price_Import:

    def readin(self):
        self.holder = open(self.file, 'r',encoding='iso-8859-1')#encoding='iso-8859-1'??
        return self.holder

    def start(self, mode):
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection.recap
        if mode == 'price':
            self.pricing = db.pricing_master_template
        elif mode == 'day':
            print('days connection')
            self.days = db.days_master_template
        #self.pricing.drop()
        self.days.drop()
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
        #add a measure for the base
    def add_base_modules(self):
                pass
                base_elements = ['In-DEX Standard Version',
                            'In-DEX Enterprise Version',
                            'In-DEX Third Party Logistics (3PL) Standard Version',
                            'In-DEX Third Party Logistics (3PL) Enterprise Version'
                            ]
                base = 'In-DEX Standard Version'
                pipeline = [{'$match':{'categories.category': base}}]
                result = self.pricing.aggregate(pipeline)
                print(result['result'])
                print('base ', base)
                self.pricing.update({'categories.$.category': base},
     {'$set':{'base_total': 0}})
                
    def add_days(self, filename):
            pass
            print('add_days')
            self.file = filename
            print(filename)
            self.document = self.readin()
            print(self.document)
            counter = 1
            for entry in self.document:
                #print(entry)
                if '$%title$%' in entry:
                    #print (entry)
                    parse = entry[10:-1]
                    print ('parsed ', parse)
                    #print(self.days)
                    self.days.insert({'name':parse,'categories':[],'overall_total': 0, 'section_no':counter})
                    #self.days.update({'section_name':parse})
                elif '$%sub$%' in entry:
                    #print (entry)
                    self.subhead = entry[6:]
                    #print ('subhead', self.subhead)
                elif '$%desc$%' in entry:
                    #print (entry)
                    desc = entry[9:-1]
                    print(desc)
                    line = {
                            'category':desc,
                            'no_days':0}
                    self.days.update({'name':parse},{'$push':{'categories':line}})
                elif '$%end$%' in entry:
                    print (counter)
                    counter = counter + 1
                    
if __name__ == "__main__":
#    tester1 = Price_Import()
#    tester1.start('price')
#    pricefile = 'static/pricing/pricing_testcase.csv'
#    tester1.writeout(pricefile)
#    tester1.add_base_modules()
#    print('pricing completed')
    day_file = 'static/pricing/daycount_testcase.csv'
    tester2 = Price_Import()
    tester2.start('day')
    tester2.add_days(day_file)
   
    print('day count completed')
    
    