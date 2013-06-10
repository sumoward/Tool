import pymongo
import ast
from collections import OrderedDict


connection_string = "mongodb://localhost"

connection = pymongo.Connection(connection_string, safe=True)
db = connection.recap
template = db.template2

#sec_no = 1
store=OrderedDict()
for sec_no in range(1,38):
   # var = 'section_'+ str(sec_no) + '_string'
    var = 'sections'
    #print (var)
   # cursor = template.find({},{var : True, '_id':False})
    cursor =template.aggregate({'$unwind':'sections'})
    
    #print ('check',cursor.count())
    
    for cur in cursor:
        for key in cur:
            #print (key)
            #print(cur[key])
            #cur = ast.literal_eval(cur)
            #print (cursor)
            store[key]=cur[key]
        
print (store)


#cursor2 =template.find()
#for cur in cursor2:
#    print(cur)