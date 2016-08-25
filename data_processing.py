import tweepy
from OAuth import tweets
from config import stop_words


def api_results(tweets):
	# filter the api data to tweets and add to new list
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

def sorted_output(wordnum):
	# changes dict to tuple then does key-value sorting
	sorted_list = {}
	sorted_list = wordnum
	keys = sorted_list.keys()
	values = sorted_list.values()
	print "{:>8} {:>8}".format('Frequency', 'Word')
	sorted_list = [(v, k) for k, v in sorted_list.iteritems()]
	for v, k in sorted(sorted_list, reverse=True):
		print "{:>5} {:<12}".format(v, k)

def get_sentiments(words):
	pass
