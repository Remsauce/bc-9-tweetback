import tweepy 
# Use Tweepy to authenticate twttrmood app with Twitter API.

consumer_key = "xshjYsQMwpDELDEeBWyaizZPD"
consumer_secret = "WzApKoj3T7NNoH8bsYR3LAYoNJ0Did9mW94o1YtfH1JcIP1u1u"
access_token = "618524731-7f0j9XCUhxX2fzo6meuVi0S3eCm8ilivKDjFE7ac"
access_token_secret = "zRYobNbv1H3WvqyY8wg8dDsvJ8Q10ZA4i5MgvDpGs3ZVY"
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
