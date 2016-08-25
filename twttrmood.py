#import clint
from OAuth import *
from data_processing import *

tweets_list = []

print '*'*50 
print ":] :/ :[ twttrmood :] :/ :[" #create blinking faces
print '*'*50 
handle = raw_input("Enter twitter handle: ")

def get_user_details(handle):  
	# into message
	user = tweets.get_user(handle)
	print "%s has %s followers!" %(user.screen_name, user.followers_count) 
	print "Here's a list of %s's favourite words:" %(handle)

get_user_details(handle)
tweets_list = api_results(get_user_tweets(handle))
list_of_words = tweets_to_words(tweets_list) 
words_without_stopwords = remove_stop_words(list_of_words)
wordnum = frequently_used_words(words_without_stopwords)
sorted_list = sorted_output(wordnum)


		

