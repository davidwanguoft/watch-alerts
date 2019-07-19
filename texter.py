from config import phone_no

import urllib3
from config import gmail_id, gmail_pw, phone_no
from email.message import EmailMessage
from email.headerregistry import Address
import os
import smtplib

# Gmail details
# email_address = os.getenv(gmail_id, None)
# email_password = os.getenv(gmail_pw, None)
email_address = gmail_id
email_password = gmail_pw

# Recipent
to_address = (
    Address(display_name='David Wang', username=phone_no, domain='msg.telus.com'),
)

def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

if __name__ == '__main__':
    msg = create_email_message(
        from_address = email_address,
        to_address = to_address,
        subject = 'Subject Header',
        body = "Test body text.",
    )

    with smtplib.SMTP('smtp.gmail.com', port = 587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print('Email sent successfully')


'''
msg = EmailMessage()
TO_MSG = [phone_no]

msg['From'] = 'davidwangswe@gmail.com'
msg['To'] = TO_MSG+'@msg.telus.com'
msg['Subject'] = 'Watch Alert'

msg.set_content('SAMPLE PLACEHOLDER TEXT')
'''