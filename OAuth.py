import tweepy, os
import json as simplejson
from config import *
# Use Tweepy to authenticate twttrmood app with Twitter API.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Create a Twitter API object called api.
#qs = handle
#tweet_results = api.search(q=qs, count=100)

def get_user_details(handle):  
# Test app-api connection by printing user details. 
	user = api.get_user(handle)
	print user.screen_name
	print user.followers_count 


def get_user_tweets(handle): 
# Test app-api connection by printing user tweets.
	user_tweets = api.user_timeline(screen_name = handle)
	for tweet in user_tweets:
		print tweet.text

