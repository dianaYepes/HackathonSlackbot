import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter



#loading our env variables -->these variables are in the .env file for security reasons.  They are tokens that should not be public
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


client = slack.WebClient(token=os.environ['BOT_TOKEN'])


#initiate flask with our file name
app= Flask(__name__)

slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)


@app.route('/question',methods= ['GET','POST'])
def recieved():
    data = request.form
    print(data)
    return Response, 200
    



#making sure we only run webserver when we have to, not if this gets imported to another file
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)



