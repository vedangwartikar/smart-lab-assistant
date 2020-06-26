<h1 align="center">Automation of Network Systems using NLP and Slack API</h1>

<div align="center">
    <img src="https://github.com/vedangwartikar/slack-automation/blob/master/slack-automation.gif" alt = "this slowpoke moves"/>
</div>
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/vedangwartikar/slack-automation/issues)
[![Forks](https://img.shields.io/github/forks/Devang-25/Face-Mask-Detection-Project.svg?logo=github)](https://github.com/vedangwartikar/slack-automation/members)
[![Stargazers](https://img.shields.io/github/stars/Devang-25/Face-Mask-Detection-Project.svg?logo=github)](https://github.com/vedangwartikar/slack-automation/stargazers)
[![Issues](https://img.shields.io/github/issues/Devang-25/Face-Mask-Detection-Project.svg?logo=github)](https://github.com/vedangwartikar/slack-automation/issues)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/vedang-wartikar-57359915a/)

## Features

Python automation scripts that can be initiated by providing natural language commands in a Slack channel which will execute on remote PCs:

- Shutdown/Restart
- Generate a Process Log file
- Send files to/from smartphone and PCs
- Install python packages
- Send routine alerts

## Usage

### Installation

You will need to:

- Install latest version of [Slack](https://slack.com/intl/en-in/downloads/android) on a smartphone
- Install [Python 3](https://www.python.org/downloads/)
- Genereate a [Slack Legacy token](https://api.slack.com/custom-integrations/legacy-tokens)

```bash
$ git clone https://github.com/vedangwartikar/slack-automation.git
$ cd slack-automation
```

- Enter the Slack Legacy token in main.py

The code is multi-platform and is tested on both Windows and Unix/Linux machines.

### How to Run

```bash
#install python dependencies from requirement.txt
$ python main.py
```

Once the code gets running on the PC, commands can be issued on the Slack channel in natural language. These commands will be interpreted on the server PC which will initiate the respective automation scripts.

## Functionalities

Slack channel commands| Description
------------ | ------------------------------------------
Shutdown | To shutdown a PC
Restart | To Restart a PC
Install python library **XYZ** | Installs any python library using pip command
Generate Process log | Sends a process log file of the PC onto the Slack channel
Send file **XYZ** | Send any specific file
Send alert | To provide routine alerts to PC
