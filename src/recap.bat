rem boot mongod
mongod --smallfiles --logpath "c:\eclipse for python\workspace\RECAP\src\"
rem pause for 6 seconds using ping command
ping -n 6 127.0.0.1>NUL
rem run recap_questionaire_module.py
start recap2.bat