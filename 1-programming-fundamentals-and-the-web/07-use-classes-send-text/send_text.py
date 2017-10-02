# You should create a config.py file containing the config variables used below
import config

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = config.twilio_sid
# Your Auth Token from twilio.com/console
auth_token  = config.twilio_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=config.my_phonenumber,
    from_=config.twilio_from_number,
    body="Hello from Python!")

print(message.sid)
