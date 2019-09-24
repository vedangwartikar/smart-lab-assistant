import os
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
	data = payload['data']
	web_client = payload['web_client']
	rtm_client = payload['rtm_client']
	if 'Shutdown' in data['text']:
		channel_id = data['channel']
		thread_ts = data['ts']
		user = data['user']

		os.system("shutdown /s /t 1");
		
		web_client.chat_postMessage(
			channel=channel_id,
			text=f"Shutdown successfull!",
			thread_ts=thread_ts
		)
	elif 'Restart' in data['text']:
		channel_id = data['channel']
		thread_ts = data['ts']
		user = data['user']

		os.system("shutdown /r /t 1");

		web_client.chat_postMessage(
			channel=channel_id,
			text=f"PC has been Restarted!",
			thread_ts=thread_ts
		
		)
slack_token = _ENTER_TOKEN_HERE_
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
