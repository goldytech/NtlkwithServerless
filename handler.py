import json
import logging
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def extract(event, context):
    #logger.info(event)
    body = event["body"]
    data = json.loads(str(body))
    if "text" not in data:
        logging.error('Validation failed')
        raise Exception('Invalid request')
    
    text = data["text"]
    sents = sent_tokenize(text)
    print(len(sents))
    assert 2 <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]
    
    response = {
        "statusCode":200,
        "body": json.dumps(word_sent)
    }
    return response

# with open('data.json','r') as txt:
#      jsondata = txt.read()

# payload = json.loads(jsondata)
# summary = extract(payload,None)
# print(summary)
    