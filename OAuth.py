import tweepy, os
import json as simplejson
from config import *

'''
Use Tweepy to manage authentication between 
twttrmood app and Twitter API.
'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Twitter API object called api.
api = tweepy.API(auth)


# Test app-api connection by printing user details.
def get_user_details(handle):  
	user = api.get_user(handle)
	print user.screen_name
	print user.followers_count 


def get_user_tweets(handle): 
	user_tweets = api.user_timeline(screen_name = handle)
	for tweet in user_tweets:
		print tweet.text


