import tweepy
from api.twitter_keys import getKeys

#######################################
# Get Twitter API keys
access_token, access_secret, consumer_key, consumer_secret = getKeys()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
myAPI = tweepy.API(auth)
#######################################

class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print("\nIncoming tweet by "+status.author.screen_name+":")
		print(status.text)

	def on_error(self, status_code):
		if status_code == 420:
			return False


#######################################

def stream_listener():
    stream_listener = StreamListener()
    print("Stream Starting...\n")
    stream = tweepy.Stream(auth=myAPI.auth, listener=stream_listener)
    stream.filter(track=["@paul2greasy"])
