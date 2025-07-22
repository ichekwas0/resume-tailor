from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_mail(message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "TAILORED RESUME"
    msg['From'] = os.getenv('GMAIL_SENDER')
    msg['To'] = os.getenv('GMAIL_RECEPIENT')

    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(os.getenv('GMAIL_SENDER'), os.getenv('GMAIL_KEY'))
        smtp.send_message(msg)