import slack
import sys

@slack.RTMClient.run_on(event='message')
def slack_auto(**payload):
	data = payload['data']
	web_client = payload['web_client']
	rtm_client = payload['rtm_client']
	channel_id = data['channel']
	thread_ts = data['ts']
	#user = data['user']
	try:
		if 'Shutdown' in data['text']:
			import shutdown
			shutdown.execute(web_client, data, channel_id, thread_ts)
		elif 'Restart' in data['text']:
			import restart
			restart.execute(web_client, data, channel_id, thread_ts)
		elif 'Install' in data['text']:
			import package_installation
			package_installation.execute(web_client, data, channel_id, thread_ts)
		elif 'Process log' in data['text']:
			import processlog
			processlog.execute(slack_token)
		elif 'Send file' in data['text']:
			import file
			file.execute(slack_token, data)
		elif 'Alert' in data['text']:
			import alert
			alert.execute()
		elif 'Help' in data['text']:
			import help
			help.execute(slack_token, data)
		elif 'Exit' in data['text']:
			sys.exit()
	except:
		print(sys.exit())

slack_token = 'xoxp-754552798980-756882538807-764678931828-0de6562a1ff19219d49870d892fc1164' #Enter Slack token
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
