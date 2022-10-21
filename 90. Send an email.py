import smtplib

sender = 'timosmatlabcach@gmail.com'
receiver = 't.roolant@student.fontys.nl'
password = 'Matlab123'
subject = 'Python email test'
body = 'I wrote an email'

#Header
message = f""" From: {sender}
To: {receiver}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 465)
server.starttls()

server.login(sender,password)

print("logged in")

server.sendmail(sender,receiver,message)
print("Email has been send")

