'''
Created on 22 May 2013

@author: brian
'''
from mailmerge import MailMerge
import requests
import base64

API = 275297545
API_URI = "http://do.convertapi.com/word2pdf/json"
afilename = 'test.docx'


class DocGen:

    def importfile(self, filename):
        f = open(filename, "r")
        text = f.read()
        print (text)
        return text

    def mail_merge(self, template, kwargs):

        company_name = kwargs.get('Company_Name', "default company_name")
        print('******', company_name)
        print('*******************', kwargs.items())
        print('********', template)
        document = MailMerge(template)
        print (document.get_merge_fields())
        #merge fields
        #{'ZIP_Code', 'Address_Line_2', 'Country_or_Region',
        #'Address_Line_1', 'Company_Name', 'Title',
        # 'State', 'City', 'First_Name', 'Work_Phone',
        #'Email_Address', 'Home_Phone', 'Last_Name'}

        document.merge(Title=kwargs.get('Title', "default title"),
                First_Name=kwargs.get('First_Name', "default fname"),
                Last_Name=kwargs.get('Last_Name', "default lname"),
            Company_Name=kwargs.get('Company_Name', "default company_name"),
                Email_Address=kwargs.get('Email_Address', "default email"),
                City=kwargs.get('City', "default city"),
                State=kwargs.get('State', "default state"),
                Work_Phone=kwargs.get('Work_Phone', "default Work Phone"),
                Address_Line_1=kwargs.get('Address_Line_1', "Address_Line_1"),
        Address_Line_2=kwargs.get('Address_Line_2', "default Address_Line_2"),
                Home_Phone=kwargs.get('Home_Phone', "Home_Phone"),
Country_or_Region=kwargs.get('Country_or_Region', "default Country_or_Region"),
                    ZIP_Code=kwargs.get('ZIP_Code ', "default ZIP_Code "))

        output =  company_name + '_output.docx'
        document.write(output)
        #print(output, ' is ready')
        return  output

    def convert(self, filename, output):
        #print('*' * 70)
        payload = {'OutputFileName': output, 'ApiKey': ''}
        files = {'file': open(filename, 'rb')}
        result = requests.post(API_URI, files=files, data=payload)
        #print(result.headers)
        print('*' * 70)
        #read document as json
        pdf = result.json()['File']
        #decode document from base64
        pdf = base64.b64decode(pdf.encode('ascii'))
        #write out the document as binary
        f1 = open(output, 'wb')
        f1.write(pdf)
        print('completed conversion')


if __name__ == "__main__":
    print('test  document generation')
    doc2 = DocGen()
    template = 'static/documents/Executive_Summary2.docx'
    #company_name = 'Principalx Systems'
    company_data = {'Title': 'Mr',
                        'First_Name': 'Joe',
                        'Last_Name': 'OShea',
                        'Company_Name': 'Principal Systems',
                        'Email_Address': 'joeoshea@principalsystems.com',
                        'City': 'Dublin',
                        'State': 'Dublin',
                        'Work_Phone': '123333',
                        'Address_Line_1': '56 Pembrooke road',
                        'Address_Line_2': 'Ballsbridge',
                        'Home_Phone': '1234567',
                        'Country_or_Region': 'Ireland',
                        'ZIP_Code': 'Dublin6'}

    print('Begin mail merge for ', company_data)
    filename = doc2.mail_merge(template, company_data)
    print(filename,' is your document')

    output1 = 'static/documents/' + filename[:-5] + '.docx'
    output2 = 'static/documents/' + filename[:-5] + '.pdf'
    print(output1)
    doc2.convert(filename, output1)
    doc2.convert(filename, output2)
    print('end of test')
