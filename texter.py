from config import phone_no

import urllib3
from email.message import EmailMessage


msg = EmailMessage()
TO_MSG = [phone_no]

msg['From'] = 'mail@something.ca'
msg['To'] = TO_MSG+'@msg.telus.com'
msg['Subject'] = 'Watch Alert'

msg.set_content('SAMPLE PLACEHOLDER TEXT')
