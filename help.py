import requests

def execute(slack_token, data):
	filename = "help.txt"
	my_file = {'file' : (filename, open(filename, 'rb'))}
	payload={
	"filename":filename, 
	"token":slack_token, 
	"channels":['#general'], 
	}

	r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
	print("Help file succesfully uploaded on Slack channel")
