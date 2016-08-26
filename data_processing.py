#from __future__ import unicode_literals
import tweepy
from OAuth import *
from config import stop_words, apikey
import simplejson as json 
from watson_developer_cloud import AlchemyLanguageV1

'''
Functions to process the raw Twitter data and output into an ordered tuple of
words. 
'''

def get_user_details(handle):  
	# intro message
	user = tweets.get_user(handle)
	print "\n%s has %s followers!" %(user.screen_name, user.followers_count) 
	print "\nHere's a list of %s's favourite words:\n" %(handle)

def api_results(tweets):
	# extract tweets from the api data and add to new list
	tweets_list = []
	for tweet in tweets:
		tweets_list.append(tweet.text)
	return tweets_list

def tweets_to_words(tweets_list):
	# convert tweets to a list of words, excluding the tweet ID
	list_of_words = []
	for tweet in tweets_list:
		list_of_words += tweet.title().split()
	return unicode_to_string(list_of_words)

def unicode_to_string(list_of_words):
	# convert unicode words to lowercase string 
	string_words = []
	for word in list_of_words:
		string_words.append(word.encode('utf-8').lower())
	return string_words

def remove_stop_words(list_of_words):
	# removes the stop-words from the list of words.
	words_without_stop_words = []
	for word in list_of_words:
		if word not in stop_words:
			words_without_stop_words.append(word)
	return words_without_stop_words

def frequently_used_words(words):
	wordnum = {}
	for word in words:
		if word not in wordnum:
			wordnum[word] = words.count(word)
	return wordnum

'''
Changes dict to tuple then does key-value sorting
'''
def sorted_output(wordnum): 
	sorted_list = {}
	sorted_list = wordnum
	keys = sorted_list.keys()
	values = sorted_list.values()
	print "{0} \t {1}".format('Frequency', 'Word')	
	sorted_list = [(v, k) for k, v in sorted_list.iteritems()]
	for v, k in sorted(sorted_list, reverse=True):
		if v >= 5:
			print "{0} \t\t {1}".format(v, k) 

def get_sentiments(handle):

	'''Alchemy language API sentiment and emotion analysis'''
	alchemy_language = AlchemyLanguageV1(api_key=apikey)
	result_s = (json.dumps(
	  	alchemy_language.sentiment(
	   	 url='https://mobile.twitter.com/%s' % (handle)), 
	  	indent=2))
	sentiment = json.loads(result_s)
	
	print '\n'
	print emojii 
	print "\n\t %s's twitter:" % (handle)
	print "\t The overall sentiment is:", sentiment['docSentiment']['type'].upper()

	result_e = (json.dumps(
	alchemy_language.emotion(
	     	url='https://mobile.twitter.com/%s' % (handle)), 
	   	indent=2))
	emotion = json.loads(result_e)

	print "\t The overall emotions are:"#, emotion['docEmotions'][]

	print '\t Anger: ', emotion['docEmotions']['anger']
	print '\t Joy: ', emotion['docEmotions']['joy']
	print '\t Fear: ', emotion['docEmotions']['fear']
	print '\t Sadness: ', emotion['docEmotions']['sadness']
	print '\t Disgust: ', emotion['docEmotions']['disgust']
	print '\n'
	print emojii2
	print '\n'