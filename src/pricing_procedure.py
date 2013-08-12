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
        print('get pricing for section ' + str(section_no) + ' of ' + username)
        pipeline = [{'$match' : { 'section_no' : section_no } }]
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


if __name__ == "__main__":
    pricing1 = Pricing_procedure()
    #tester1 = Database_manage_recap()
    username = "aad"
    username = username + '_pricing'
    temp = pricing1.set_pricing(username)
    print(temp)
    section_no = 1
    username = 'aad'
    pricing1.get_pricing(section_no, username)
    username = 'aad'
    boo =pricing1.check_pricing_exist(username)
    print(boo)
    


