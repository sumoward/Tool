# -*- coding: iso-8859-1 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP
"""
mail handling class for recap.
It allows for attachments and uses ga,il for smtp.
"""


class Email_handler():

    def build_mime(self, filename, customer):

        LOGIN = "principalsystemsie@gmail.com"
        PASSWORD = "Number56"
        msg = MIMEMultipart()
        msg['Subject'] = 'Email From RECAP about ' + str(filename)
        msg['From'] = LOGIN
        msg['Reply-to'] = ''
        #email a copy to our gmail for records
        msg['To'] = customer + ' , ' + LOGIN
        # That is what u see if dont have an email reader:
        msg.preamble = 'Multipart message.\n'
        # This is the textual part:
        part = MIMEText("Hello. \n A new file \
        " + str(filename) + " has been uploaded for this account.\
        \nI am sending an email from a Python program,\
         just testing.\n The attachment should work")
        msg.attach(part)
        print ('filename: ',filename)
        for file in filename:
            # This is the binary part(The Attachment):
            part = MIMEApplication(open(file, "rb").read())
            part.add_header('Content-Disposition',
                             'attachment', filename=file)
            msg.attach(part)
        # Create an instance in SMTP server
        smtp = SMTP("smtp.gmail.com", 587)
        # Start the server:
        #uncomment this if you wish to debug
        #smtp.set_debuglevel(1)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(LOGIN, PASSWORD)
        # Send the email
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

if __name__ == "__main__":
    handler = Email_handler()
    filename1 ='static/downloads/ASN & Pallet and Case Label Data Capture Template.xlsx'
    filename2 = 'static/downloads/Customer charges.xlsx'
    filename=[filename1, filename2]
    customer = 'brian.ward@principalsystems.com'
    handler.build_mime(filename, customer)
