# Libraries
import tweepy
import json

# Import Twitter Keys
from api.twitter_keys import getKeys



""" Log into Twitter """
access_token, access_secret, consumer_key, consumer_secret = getKeys()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
API = tweepy.API(auth, wait_on_rate_limit=True)


""" Grab Tweets """
searchQueries = ["#browns", "#buccaneers"]
brownsTweets = []
buccaneersTweets = []
bofTweets = []

for query in searchQueries:
    for status in tweepy.Cursor(API.search, q=query).items(10):
        statusText = status.text.lower()
        if all(x in statusText for x in searchQueries):
            print("bof")
        elif "#browns" in statusText:
            print("#browns")
        elif "#buccaneers" in statusText:
            print("#buccaneers")
