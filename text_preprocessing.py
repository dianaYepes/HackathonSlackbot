import spacy
from string import punctuation

load_nlp = spacy.load("en_core_web_sm")

def fetch_keywords(text):
    tokens = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
    doc = load_nlp(text.lower()) 
    for token in doc:
        if(token.text in load_nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            tokens.append(token.text)
    return tokens

text = """
We are gathered here today on this joyous occasion to celebrate the special love that Monica and Chandler share. It is a love based on giving and receiving as well as having and sharing. And the love that they give and have is shared and received. And
through this having and giving and sharing and receiving, we too can share and love and have... and receive.
"""

# text ="""
# Where can I find the NES packages on github?
# """

keyword_list = list(set(fetch_keywords(text)))
print(keyword_list)
