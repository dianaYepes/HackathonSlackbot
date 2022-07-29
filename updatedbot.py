from pickle import TRUE
import slack
import os
import spacy
import json
import threading
import requests
from string import punctuation
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import blockText
load_nlp = spacy.load("en_core_web_sm")

tsMaps = {}



#loading our env variables -->these variables are in the .env file for security reasons.  They are tokens that should not be public
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
key = os.environ.get('BOT_TOKEN')
client = WebClient(token = key)


#initiate flask app with our file name
app= Flask(__name__)



#function that filters most important keywords (we get rid of puntuation and stopwords and only care for adj,nouns,propn)
#review what thelma sent you for thge inline coding, perhaps you can use that and replace this one or just add it in.  
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


#go through slack channel history adding the messages to list
def findRelevantMessages(channel_name,textList):
    conversation_history = []
    conversation_history_link = []
    conversation_id = None


 #might change things here since if we pass the channel_id directly we don't need to waste time looping through channels and conversation list
 #we can just directly access channel conversation history
    try:
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


    keywords = textList
    jsonObject = {}
    jsonList=[]
    for i, message in enumerate(conversation_history):

        #here we set up a ranking system to check the top 4 (maybe 5)? messages containing the MOST keywords, not just of they have any of the keywords
        #this will make results more accurate
        # are there maybe other ways to improve accuracy?

        if any(x in message["text"] for x in keywords):
            link=conversation_history_link[i]["permalink"]
            jsonObject = {
                "resultLink": link
            }
            if len(jsonList)>4:
                break
            else:
                jsonList.append(jsonObject)
    json.dumps(jsonList)
    return(jsonList)




#this app is invoked when button is pressed
@app.route('/block_actions',methods= ['GET','POST'])
def messageInteractions():
    buttonLoad = request.form
    dictnow = json.loads(buttonLoad['payload'])
    parentTs = dictnow['container']['message_ts']
    channel_id = dictnow['container']['channel_id']
    buttonPressed = dictnow['actions'][0]['text']['text']
    helpfulLink = dictnow['actions'][0]['value']
    res = dictnow['response_url']
    if buttonPressed == "Helpful?":
        client.chat_postMessage(channel=channel_id, thread_ts=tsMaps[parentTs], text=helpfulLink)
        requests.post(res,json={"delete_original":"true"})
    if buttonPressed == "Not Helpful":
        requests.post(res,json={"delete_original":"true"})
    del tsMaps[parentTs]
    return Response(),200


#here we retrieve the question, call the functions to parse keywords and get most valuable suggestions,
#and then form and post the ephemeral suggestions message.  Notice we add the ephemeral message ts as key to posted message ts as value in dictionary
@app.route('/question',methods= ['GET','POST'])
def recieved():
    form = request.form
    print(form)
    question = form['text']
    user = form['user_name']
    channel_name = form['channel_name']
    channel_id=form['channel_id']
    user_id=form['user_id']
    def do_work(channel_name,question):
        posted = client.chat_postMessage(channel=channel_name,text=question, username=user)
        textList= (fetch_keywords(question))
        jsonList=(findRelevantMessages(channel_name,textList))

        if len(jsonList) > 1:
            del jsonList[0] 
            suggestion = blockText.Suggestions(channel_id,user_id,jsonList)
            message = suggestion.getmessage()
            response = client.chat_postEphemeral(**message)
            tsMaps[response['message_ts']] = posted['ts']

        else:
            print("nothing found")
    thread = threading.Thread(target=do_work, args=(channel_name,question))
    thread.start()
    return Response(),200

   

#making sure we only run webserver when we have to, not if this gets imported to another file
if __name__ == '__main__':
    app.run(debug=True)



