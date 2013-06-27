import unittest
from database_manage import Database_manage_recap


class TestSequenceFunctions(unittest.TestCase):

    def test_dbconnection(self):
        tester1 = Database_manage_recap()
        username = 'testercompany'
        answer = str(tester1.dbconnection(username))
        #print('ans: ', type(answer))
        self.assertEqual(answer,
         "Collection(Database(MongoClient('localhost', 27017), 'recap'), 'testercompany')",
         "It should read dCollection(Database(MongoClient('localhost', 27017),'recap'), 'testercompany')")

    def test_copy_template(self):
        tester1 = Database_manage_recap()
        username = 'testercompany'
        tester1.dbconnection(username)
        answer = tester1.copy_template()
        #print('ans: ', type(answer))
        self.assertEqual(type(answer), dict," the method should return a dictionary")

    def test_create_interface_dict(self):
        page = 'sales'
        customer_name = 'testercompany'
        tester1 = Database_manage_recap()
        tester1.dbconnection(customer_name)
        #tester1.copy_template()
        answer = tester1.create_interface_dict(page, customer_name)
        print('ans: ', type(answer))
        print('ans: ', (answer))

    def test_check_create_db(self):
        customer_name = 'testercompany'
        tester1 = Database_manage_recap()
        answer = tester1.check_create_db(customer_name)
        #print('ans',answer)
        self.assertEqual(answer, customer_name," the method should return a dictionary")

if __name__ == '__main__':
    unittest.main()
