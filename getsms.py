#!/usr/bin/env python
# md5: 13e1b2ff3188adf4f622a8ceca2e26b8
#!/usr/bin/env python
# coding: utf-8



# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from getsecret import getsecret

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = getsecret('TWILIO_SID')
auth_token = getsecret('TWILIO_AUTH_TOKEN')



client = Client(account_sid, auth_token)



from datetime import datetime, timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)



from flask import Flask
app = Flask(__name__)

@app.route('/get_sms_cs377')
def get_sms_cs377():
  output = []
  messages = client.messages.list(limit=5)
  for record in messages:
    output.append('|'.join([str(utc_to_local(record.date_sent)), record.direction, record.body]))
  return '\n'.join(output)

@app.route('/')
def hello_world():
  return 'Nothing to see here'

if __name__ == '__main__':
  app.run()

