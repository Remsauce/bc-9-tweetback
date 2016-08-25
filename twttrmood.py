import emoji
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from data_processing import *
from progress_bar import progress_bar

'''
Application entry point. 
'''

tweets_list = []

print '*'*50 
print (emoji.emojize(':laughing: :cry: :smiling_imp: :dizzy_face:', use_aliases=True))
cprint(figlet_format('twttrmood', font='ogre'),
           'green', attrs=['bold'])
print (emoji.emojize(':joy: :rage: :yum: :cupid:', use_aliases=True))
print '*'*50
handle = raw_input("Enter twitter handle: ")

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