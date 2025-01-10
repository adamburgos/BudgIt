import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

def send_sms(to_number, message_body):
    client = Client(account_sid, auth_token)

    message = client.message.create (
        body=message_body,
        from_=twilio_number,
        to=to_number
    )
    
    print(f"Message sent! SID: {message.sid}, Status: {message.status}")
