import subprocess

def execute(web_client, data, channel_id, thread_ts):
	words = data['text'].split()
	command = "pip install " + words[1]
	subprocess.call(command, shell = True)
	txt = "Successfully installed " + words[1]
	web_client.chat_postMessage(
		channel=channel_id,
		text=txt,
		thread_ts=thread_ts

	)