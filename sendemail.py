import smtplib

senders = 'romario1995martin@gmail.com'

receivers = 'romarioomartin@gmail.com'

from_name="Genius"
msg="Well well well"
to_name="Wife a wife"
subject="Well"
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
""" 

#message_to_send1 = message.format(from_name,from_email,to_name,receivers,subject,msg) 
message_to_send2 = message.format(

                             from_name,

                             senders,

                             to_name,

                             receivers,

                             subject,

                             msg)
username = ''#Enter username
password = ''#Enter AppPassword
   # The actual mail sender
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(senders, receivers, message_to_send2)
#print "Successfully sent email"
server.quit()
#except SMTPException:
 #  print "Error: unable to send email"
# Credentials (if needed)
    