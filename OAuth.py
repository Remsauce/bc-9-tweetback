import tweepy
import json as simplejson
from config import *
import progressbar

'''
Use Tweepy to manage authentication between 
twttrmood app and Twitter API.
'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create a Twitter API object called tweets which establishes the connection.
tweets = tweepy.API(auth) 

def get_user_tweets(handle): 
	# fetch timeline tweets from a specified user's handle
	user_tweets = tweets.user_timeline(screen_name = handle, count = 200)
	return user_tweets

