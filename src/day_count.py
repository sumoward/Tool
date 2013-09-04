from database_manage import Database_manage_recap
import pymongo
class Day_count_procedure:

    def set_daycount(self, username):
        pass
        username = username + '_days'
        print('username : ', username)
        print('set_days')
        tester1 = Database_manage_recap()
        self.store = tester1.dbconnection(username, 'days_master_template')
        temp = tester1.copy_template()
        #print(temp)
        return temp


    def get_daycount(self, section_no, username):
        username = username + '_days'
        print('username : ', username)
        pipeline = [{'$match' : { 'section_no' : int(section_no)} }]
        #cursor = self.store.aggregate(pipeline)
        connection = pymongo.MongoClient("localhost", 27017)
        db =  connection.recap
        cursor = db[username].aggregate(pipeline)
        print ('cur',cursor)
        cursor = cursor['result']
        print (cursor)
        return cursor

    def check_day_count_exist(self, username):
        pass
        username = username + '_days'
        print('username : ', username)
        connection = pymongo.MongoClient("localhost", 27017)
        db = connection['recap']
        print(db.collection_names())
        if username in db.collection_names():
            print('true')
            return True
        else:
            print('false')
            return False

    def calculate_days_total(self, username, section_no, values):
        username = username + '_days'
        section_no = int(section_no)
        #print('username : ', username, 'section : ', section_no, 'values : ', values)
        connection = pymongo.MongoClient("localhost", 27017)
        db =  connection.recap
        #update individual day counts
        for x, value in enumerate(values):
                try:
                    value = int(value)
                except: 
                    value = 0
                #print(x, value)
                db[username].update({'section_no': section_no},
     {'$set': {'categories.'+ str(x) +'.no_days': value}})
        #update teh total
        try:
            total_day_count = sum([(float(x)) for x in values])
        except:
            total_day_count = 0
        db[username].update({'section_no': section_no},
     {'$set':{'overall_total':total_day_count }})

if __name__ == "__main__":
    day1 = Day_count_procedure()
    #tester1 = Database_manage_recap()
    username = "brian"
    temp = day1.set_daycount(username)
    print('==>', temp)
    section_no = 1
    day1.get_daycount(section_no, username)
    day1.check_day_count_exist('elaine')
    day1.check_day_count_exist(username)
    section_no = '1'
    values =['1', '2', '3', '0', '0', '0', '0', '0', '8']
    day1.calculate_days_total(username, section_no, values)
    
    