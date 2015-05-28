__author__ = 'Chris'

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

#To keep keys secret, left them in a keys.txt file and read them to vars
with open('keys.txt', 'r') as f:
    consumer_key = f.readline().rstrip()
    consumer_secret = f.readline().rstrip()
    access_token = f.readline().rstrip()
    access_secret = f.readline().rstrip()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

