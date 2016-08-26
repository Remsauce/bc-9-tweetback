import config
from termcolor import cprint
from pyfiglet import figlet_format
from data_processing import *
from progress_bar import progress_bar


'''
Application entry point. 
'''

tweets_list = []

print '*'*50 
print emojii, emojii
cprint(figlet_format('twttrmood', font='ogre'),
           'green', attrs=['bold'])
print emojii2, emojii2
print '*'*50
handle = raw_input("\nEnter twitter handle: \n")

'''
All functions are called from this point.
'''
get_user_details(handle)
progress_bar()
tweets_list = api_results(get_user_tweets(handle))
list_of_words = tweets_to_words(tweets_list) 
words_without_stopwords = remove_stop_words(list_of_words)
wordnum = frequently_used_words(words_without_stopwords)
sorted_list = sorted_output(wordnum)
get_sentiments(handle)