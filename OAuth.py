import tweepy 
# Use Tweepy to authenticate twttrmood app with Twitter API.

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Create a Twitter API object called api.

def get_user_details(handle = ''):  
# Test app-api connection by printing user details. 
	user = api.get_user(handle)
	print user.screen_name
	print user.followers_count 
	for friend in user.friends():
   		print friend.screen_name


def get_user_tweets(handle = ''): 
# Test app-api connection by printing user tweets.
	user_tweets = api.user_timeline(screen_name = handle)
	for tweet in user_tweets:
		print tweet.text

get_user_details('rehemaw')
get_user_tweets('rehemaw')
