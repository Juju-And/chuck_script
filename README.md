# Chuck script

This is a simple Python application intended to raffle Chuck Norris jokes from the database (http://api.icndb.com/jokes/random)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install requirements.txt
```

### Installing

First step is to run the first file in order to get the first joke:

```
$ python3 chuck_sctipt.py 
```

the other instructions would be presented in the terminal (getting a new joke or quitting).


In order to be able to present jokes on Slack, slack_token should be updated with channels legacy-token:

```
    slack_token = os.environ.get('SLACK_TOKEN')
```