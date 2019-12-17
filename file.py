import requests

def execute(slack_token, data):
	words = data['text'].split()
	filename = words[2]
	my_file = {'file' : (filename, open(filename, 'rb'))}
	payload={
	"filename":filename, 
	"token":slack_token, 
	"channels":['#general'], 
	}

	r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
	print("File succesfully uploaded on Slack channel")