import smtplib # libary
from email.message import EmailMessage # this pakage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('nakkamanikanta1903@gmail.com','mqhv bzsl gbpj nkeu')
    msg=EmailMessage()
    msg['FROM']='nakkamanikanta1903@gmail.com'
    msg['To']=to
    msg['SUBJECT']=subject
    msg.set_content(body) #otp body for visiable
    server.send_message(msg)
    server.close()