import os
from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hey Sal is this you on board my spaceship?',
         from_='+twilio_number',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='+number_wanting_to_send_to'
     )

print(message.sid)