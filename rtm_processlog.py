from __future__ import unicode_literals
import psutil
import os
import sys
import time
import slack
import requests
from slack import WebClient


slack_token = '' #Enter Slack Legacy Token Here
client = slack.WebClient(token=slack_token)

def process(log_dir = "Log"):

	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass
	separator = '-' * 80
	ct = ""
	currtime = str(time.ctime())
	for i in currtime:
		if i == ':':
			i = '.'
		ct += i
	
	log_path = os.path.join(log_dir, "Process Log at %s.log" %ct)
	fd = open(log_path, 'x')
	fd.write(separator + "\n")
	fd.write("Process Log at "+time.ctime()+"\n")
	fd.write(separator + "\n")
	processlist = []

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])
			pinfo['vms'] = proc.memory_info().vms / (1024*1024)
			processlist.append(pinfo)

		except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

	for element in processlist:
		fd.write("%s\n"%element)

	print("Process log succesfully created at ", ct)
	return log_path

def main():
	print("Process Monitor: ")

	filename = process(sys.argv[1])
	print(filename)

	my_file = {'file' : (filename, open(filename, 'rb'), 'txt')}
	payload={
	"filename":filename, 
	"token":slack_token, 
	"channels":['#general'], 
	}

	r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
	print("File succesfully uploaded on Slack channel")

if __name__ == '__main__':
	main()	
