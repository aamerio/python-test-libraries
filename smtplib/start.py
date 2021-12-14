import os
from email.message import EmailMessage
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()
smtp_host = os.getenv('SMTP_HOST')
smtp_port = os.getenv('SMTP_PORT')
username = os.getenv('SMTP_USER')
password = os.getenv('SMTP_PASS')
textfile = "email-text.txt"
email_from = "from@example.com"
email_to = "to@example.com"

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = email_from
msg['To'] = email_to

# Send the message via our own SMTP server.
smtp = SMTP(smtp_host, smtp_port)
smtp.login(username, password)
smtp.send_message(msg)
smtp.quit()
