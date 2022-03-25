#send mail to me through python script
#keep cc to other two if naga is writing script she will keep radha and shivani in cc

import smtplib

sent_from= 'lakshmi73862@gmail.com'
gmail_password = 'uhfpojsksibkvwwz'

to = ['vibha.rawan@neosoftmail.com']

cc = ["grandheraj68@gmail.com", "radha.maredi@gmail.com"]
bcc = ["arun.nadar@neosoftmail.com", "rohan.dhere@neosoftmail.com"]

subject = 'Introduction'
body = 'Hello, Iam Nagalakshmi. This email is sent through Python script.'

email_text = """\
From: %s
To: %s
Subject: %s
cc: %s
bcc: %s
%s
""" % (sent_from, ", ".join(to), subject,", ".join(cc), ", ".join(bcc), body)

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(sent_from, gmail_password)
smtp_server.sendmail(sent_from, to + cc + bcc, email_text)
smtp_server.close()
print ("Email sent successfully!")
