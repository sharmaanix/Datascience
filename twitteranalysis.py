import tweepy
from textblob import TextBlob

consumer_key = 	'lwrVsBgqg1MzXItVtrmKAsaLh'
consumer_secret = 'AsAwjFaYkFho7LilVjyEeSde2zlTPFFDDL9s8GRwVoTVCe8ogd'

access_token = '1255986152-RBz1mmHC0lgX3FYfxIIMuGnxgof0GQIFjjT9kiq'
access_token_secret = '0kg8M0J2GBOOXiUtBOo1Q34OP90WDq2MCiNGT6NqjB07Y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
pub_tweets = api.search('@aveloroy')

for tweet in pub_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
