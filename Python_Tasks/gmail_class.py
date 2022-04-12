#send mail to me through python script
#keep cc to other two if naga is writing script she will keep radha and shivani in cc

import smtplib

class PythonMail:

    def __init__(self, to, cc, bcc):

        """Initializing instance attributes where these storing email addresses."""

        self.to = to
        self.cc = cc
        self.bcc = bcc


    def sending_email(self):
        
        """Sending mail through python script sending email addresses 
        as arguments and in result succesful message is printed on console 
        when email is sent to the specified addresses."""

        from_mail = 'lakshmi73862@gmail.com'
        password = 'uhfpojsksibkvwwz'

        subject = "Introduction"
        body = "Hello, Iam Nagalakshmi. This email is sent through Python script."

        message = f'To: {self.to} \rCc: {", ".join(self.cc)} \r\nSubject: {subject}\n\n{body}'
        
        #puts the connection to the SMTP server into SSL mode.
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        smtp_server.login(from_mail, password)
        smtp_server.sendmail(from_mail, [self.to] + self.cc + self.bcc, message)
        smtp_server.close()
        print ("Email is sent Successfully!")


#Create instance of PythonEmail class
email1 = PythonMail("vibha.rawan@neosoftmail.com", ["grandheraj68@gmail.com", "radha.maredi@gmail.com"], ["arun.nadar@neosoftmail.com", "rohan.dhere@neosoftmail.com"])

#calling instance method using class object 
email1.sending_email()