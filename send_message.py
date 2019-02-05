#script to send payment reminder
#source: https://www.twilio.com/docs/sms/quickstart/python

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACa1633bf314a3afd2d16873b995ba8a6c'
auth_token = 'fae57a0d2eecd2516304f1e44581013d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Expecting cloud cover for 48 hours. Please reduce your usage to improve your device performance!",
                     from_='+19843648643',
                     to='+19193232754'
                 )

print(message.sid)
