# -*- coding: iso-8859-1 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP
"""
mail handling class
"""


class Email_handler():

    def build_mime(self, filename):
        msg = MIMEMultipart()
        msg['Subject'] = 'Email From Python about ' + filename
        msg['From'] = 'brian@principal.ie'
        msg['Reply-to'] = ''
        msg['To'] = 'brian.ward@principalsystems.com'

        # That is what u see if dont have an email reader:
        msg.preamble = 'Multipart message.\n'

        # This is the textual part:
        part = MIMEText("Hello. \n A new file \
        " + filename + " has been uploaded for this account.\
        nI am sending an email from a python program,\
         just testing.\n There is also an attachment,\
         we can pretend that its from recap")
        msg.attach(part)

        # This is the binary part(The Attachment):
        part = MIMEApplication(open("persistence.txt", "rb").read())
        part.add_header('Content-Disposition',
                         'attachment', filename="persistence.txt")
        msg.attach(part)
        # Create an instance in SMTP server
        "89.101.215.10"
        smtp = SMTP("mail.principalsystems.com", 25)
        # Start the server:
        smtp.ehlo()
        #smtp.login("Brian.Ward@principalsystems.com", "Br!@nW@RD")

        # Send the email
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

if __name__ == "__main__":
    handler = Email_handler()
    filename ='recap.bat'
    handler.build_mime(filename)
