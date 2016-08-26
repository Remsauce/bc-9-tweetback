import os
import emoji

'''
Twitter API authentication - you will need to register an app
on the Twitter dev website to generate your consumer and access keys. 
'''
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

'''
 Alchemy language API authentication - you will need to sign-up
 on their website to receive an apikey
'''
url = "https://gateway-a.watsonplatform.net/calls"
apikey = ""

# stop_words filter.
stop_words = ['&amp;', 'rt', 'photo:', 'photoset: ', 'video: ', '...', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they',
         'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't',
         'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was',
         'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at',
         'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once', '"the', '"it', '"i', '"do']

#emoji
emojii = emoji.emojize('\t:laughing: :cry: :smiling_imp: :dizzy_face: :stuck_out_tongue_closed_eyes: :imp: :joy: :rage: :yum: :cupid: :kissing_heart: :weary: :sleeping:', use_aliases=True)
emojii2 = emoji.emojize('\t:joy: :rage: :yum: :cupid: :kissing_heart: :weary: :sleeping: :laughing: :cry: :smiling_imp: :dizzy_face: :stuck_out_tongue_closed_eyes: :imp:', use_aliases=True)
 