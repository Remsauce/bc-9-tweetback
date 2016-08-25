from OAuth import tweets
import tweepy
#from stop_words import get_stop_words


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

	stop_words = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they',
         'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't',
         'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was',
         'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at',
         'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']

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


def get_sentiments(words):
	pass
