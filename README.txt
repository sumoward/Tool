This is  an application to gather sales data for Warehouse management Implementation

mongoexport -d recap -c users -o users.txt


mongoimport --db recap --collection users --file users.txt


Run sonar / start

then sonar-runner in recap folder

git add -u

scp test.txt ubuntu@54.228.195.27:recap


remmeber to set root path for static files on ubuntu server
