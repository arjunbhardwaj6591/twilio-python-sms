#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install twilio


# In[ ]:


import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='This is the ship that made the Kessel Run in fourteen parsecs?',
    from_='enter your twilio no',
    to='enter your number'
)

print(message.sid)

