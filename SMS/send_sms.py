import os
from twilio.rest import Client

account_sid = 'AC32e54db222de97c784375829f45385b5'
auth_token = 'b0a073cb2f480dcc8077e4739165d173'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I know your little secret. That is coffee brew beer",
                     from_='+14752646250',
                     to='+16475046219'
                 )

print(message.sid)
