#Script for sending email along with attachments to large number of people at same time
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass

emailfile = input("Please enter the name of the text file that includes all email addresses: ")
emailtosendfrom = input('Enter your email address to send from:  ')
msgfile = input('Please enter the text file name that includes the message you want to send out  :')
email = open(emailfile, 'r')
#toaddrs = email
with open(msgfile) as msg:
    msgbody = msg.read()
#msg = open(msgfile, 'r')
#print(msgbody)

# Credentials
password = getpass.getpass('Please enter your email password  :')
#password = input('Please enter your email password  :  ')

# Send mail
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

try:
    server.login(emailtosendfrom,password)
except smtplib.SMTPAuthenticationError:
    print ('Authentication Error.......email and password do not match\n')
    exit()

msg = MIMEMultipart()

# storing the senders email address 
msg['From']=emailtosendfrom

# storing the subject 
sub=input("Enter the subject of the mail  :")
msg['Subject'] = sub

# attach the body with the msg instance
msg.attach(MIMEText(msgbody, 'plain'))

choice=input("Do you want to send any attachment(y/n)  :")
if choice=='y':
    # open the file to be sent 
    filename = input("Enter the filename to attach  :")
    pathoffile=input("Enter the path of the file  :")
    attachment = open(pathoffile, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

with open(emailfile) as f:
    emaillist = f.readlines()
    #print(emaillist)
    newlist = [x[:-1] for x in emaillist]
    #print(newlist)
    for receiver in newlist:
        msg['To'] = receiver
        # Converts the Multipart msg into a string
        text = msg.as_string()
        server.sendmail(emailtosendfrom,receiver, text)
print("\nEmail Sent\n")
server.quit()