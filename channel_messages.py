import os
from datetime import datetime
from slack import WebClient

slack_token = _ENTER_TOKEN_HERE_
channel_name = 'general'
date_from = "2019-09-05"
date_to = "2019-09-16"

oldest = (datetime.strptime(date_from, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()
latest = (datetime.strptime(date_to, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()

sc = WebClient(slack_token)

users_list = sc.api_call("users.list")
users = {}
# print(users_list)
for user in users_list['members']:
    users[user['id']] = user['profile']['real_name']
#print(users)
channels = sc.api_call("channels.list")
channel_id = None
for channel in channels['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
if channel_id == None:
    raise Exception("cannot find channel " + channel_name)
#print(channel_id)

history = sc.channels_history(channel = channel_id)
posts_by_user = {}

#print(history)
for message in history['messages']:
	print(message['text'])
