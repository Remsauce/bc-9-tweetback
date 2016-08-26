from config import apikey
import simplejson as json 
from watson_developer_cloud import AlchemyLanguageV1

'''Alchemy language API sentiment analysis'''

alchemy_language = AlchemyLanguageV1(api_key=apikey)
result_s = (json.dumps(
  	alchemy_language.sentiment(
   	 url='https://mobile.twitter.com/KimKardashian'), 
  	indent=2))
sentiment = json.loads(result_s)

print '*'*50 
print "The overall sentiment is:", sentiment['docSentiment']['type'].upper()
print '*'*50 


result_e = (json.dumps(
alchemy_language.emotion(
     	url='https://mobile.twitter.com/KimKardashian'), 
   	indent=2))
emotion = json.loads(result_e)

print "The overall emotions are:\n", emotion['docEmotions']
print '*'*50 





