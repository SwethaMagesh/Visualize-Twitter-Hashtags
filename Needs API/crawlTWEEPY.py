
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re

# Enter Twitter API Keys
access_token = "ENTER ACCESS TOKEN"
access_token_secret = "ENTER ACCESS TOKEN SECRET"
consumer_key = "ENTER CONSUMER KEY"
consumer_secret = "ENTER CONSUMER SECRET"

# Create tracklist with the words that will be searched for
tracklist = ['#Brexit', '#brexit', '#br']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=tracklist)
