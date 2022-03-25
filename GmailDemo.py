import smtplib

From ="lakshmi73862@gmail.com"
to=["vibha.rawan@neosoftmail.com"]
cc =["grandheraj68@gmail.com", "radha.maredi@gmail.com"]
pwd="uhfpojsksibkvwwz"

text="Hello, Good Morning!  Introduce yourself?    ----  from  Naga Lakshmi"
subject="Self Introduction"


message=f'subject:{subject}\n\n{text}'


server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()       #puts the connection to the SMTP server into TLS mode.

server.login(From,pwd)
print("login in successful")

server.sendmail(From,to+cc,message)
server.close()
print("mail sent")