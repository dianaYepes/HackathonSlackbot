from pickle import TRUE
import slack
import os
import spacy
import json
from string import punctuation
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_nlp = spacy.load("en_core_web_sm")
#run spacy download en_core_web_sm 


#loading our env variables -->these variables are in the .env file for security reasons.  They are tokens that should not be public
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
key = os.environ.get('BOT_TOKEN')
client = WebClient(token = key)


#initiate flask app with our file name
app= Flask(__name__)


def fetch_keywords(text):
    tokens = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
    doc = load_nlp(text.lower()) 
    for token in doc:
        if(token.text in load_nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            tokens.append(token.text)
    print(tokens)
    return tokens


def findRelevantMessages(channel_name,textList):
    api_response = client.api_test()
    custom_search = True
    conversation_store=[]
    conversation_history = []
    conversation_history_link = []
    conversation_id = None

 
    try:
        # Call the conversations.list method using the WebClient
        for result in client.conversations_list(types='public_channel,private_channel'):
            if conversation_id is not None:
                break               
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    channel_id=channel["id"]
                    result = client.conversations_history(channel=channel_id)
                    for message in result["messages"]:
                        conversation_history.append(message)
                        response = client.chat_getPermalink( 
                            channel=channel_id,
                            message_ts=message["ts"]
                        )
                        conversation_history_link.append(response)
                    break
    except SlackApiError as e:
        print(f"Error: {e}")


    if custom_search:
        print("custom")
    else:
        pass

    keywords = textList
    jsonObject = {}
    print(conversation_history_link)
    for i, message in enumerate(conversation_history):
        if any(x in message["text"] for x in keywords):
            link=conversation_history_link[i]["permalink"]
            jsonObject = {
                "resultLink":link,
            }
            print(json.dumps(jsonObject))


@app.route('/question',methods= ['GET','POST'])
def recieved():
    data = request.form
    question = data['text']
    user = data['user_name']
    channel_name = data['channel_name']
    textList= (fetch_keywords(question))
    findRelevantMessages(channel_name,textList)
    client.chat_postMessage(channel=channel_name,text=question, username=user)
    return Response(), 200
       

#making sure we only run webserver when we have to, not if this gets imported to another file
if __name__ == '__main__':
    app.run(debug=True)



