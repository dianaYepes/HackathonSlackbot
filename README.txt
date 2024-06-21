A Hackathon python project that integrates the Slack Api in order to go through channel message history and return the most relevant results to a question asked in that Channel. It first processes the text and removes stopwords (unnecassary text noise) and then uses the the Slack API to parse through previous messages and return the most relevant results.


Setup:  To install dpendencies use pip install -r requirements.txt
also run 'spacy download en_core_web_sm' on terminal to download that module

bot.py is the main proj(and hackathon original)
updatedBot.py is after hackathon with interactive code included (it uses the class blockText.py)
