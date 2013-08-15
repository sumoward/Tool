#Brian Ward
#Principal Systems
#06/09/2012
from database_manage import Database_manage_recap
import pymongo


"""
A class to generate the appropriate pricing structure
"""


class Pricing_procedure:

    def set_pricing(self, username):
        pass
        tester1 = Database_manage_recap()
        self.store = tester1.dbconnection(username, 'pricing_master_template')
        temp = tester1.copy_template()
        #print(temp)
        return temp
    
    def get_pricing(self, section_no, username):
        username = username + '_pricing'
        print(username)
        print(type(section_no))
        print('get pricing for section ' + str(section_no) + ' of ' + username)
        pipeline = [{'$match' : { 'section_no' : int(section_no)} }]
        #cursor = self.store.aggregate(pipeline)
        connection = pymongo.MongoClient("localhost", 27017)
        db =  connection.recap
        cursor = db[username].aggregate(pipeline)
        print (cursor)
        cursor = cursor['result']
        print (cursor)
        return cursor
        
    def get_section(self):
        pass
    
    def check_pricing_exist(self, username):
        pass
        username = username + '_pricing'
        print(username)
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection['recap']
        print(db.collection_names())
        if username in db.collection_names():
            print('true')
            return True
        else:
            print('false')
            return False

    def apply_calc(self, edited_values, section_no, username):
            username= username + '_pricing'
            print('apply calc',edited_values, section_no, username)
            section_no = int(section_no)
            #edit the value in mongo
            value = 42
            pipeline = [{'$match':{'section_no':section_no}},
                                 {'$project':{'_id':0,
         'categories.list_price':'$categories.list_price'}}]


            connection = pymongo.MongoClient("localhost", 27017)
            db =  connection.recap

            result = db[username].aggregate(pipeline)
            print('agg',result)
            result = result['result'][0]['categories'][0]['list_price']
            print('agg',result)

            for x, value in enumerate(edited_values):
                value = int(value)
                #print(x, value)
                db[username].update({'section_no': section_no},
     {'$set': {'categories.'+ str(x) +'.quantity': value,
                'categories.'+ str(x) +'.sub_total': (value * int(result[x]))}})

#                self.store.update({'section_no': section_no},
#     {'$set': {'categories.'+ str(x) +'.sub_total': (value * int(result[x]))}})

        

if __name__ == "__main__":
    pricing1 = Pricing_procedure()
    #tester1 = Database_manage_recap()
    username = "brian"
    username = username + '_pricing'
    temp = pricing1.set_pricing(username)
    #print(temp)
    section_no = 1
    username = 'brian'
    pricing1.get_pricing(section_no, username)
    username = 'brian'
    boo =pricing1.check_pricing_exist(username)
    #print(boo)
    edited_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    section_no = 1
    pricing1.apply_calc(edited_values, section_no, username)

