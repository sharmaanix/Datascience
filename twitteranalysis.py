import tweepy
from textblob import TextBlob

consumer_key = 	'CONSUMER_KEY_CODE'
consumer_secret = 'CONSUMER_SECRET_CODE'

access_token = 'ACCESS_TOKEN_CODE'
access_token_secret = 'ACCESS_TOKEN_SECRET_CODE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
pub_tweets = api.search('@aveloroy')

for tweet in pub_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
