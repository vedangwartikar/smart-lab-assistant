import os

def execute(web_client, data, channel_id, thread_ts):
	
	os.system("shutdown /r /t 1");
			
	web_client.chat_postMessage(
		channel=channel_id,
		text=f"Restart successfull!",
		thread_ts=thread_ts
	)
