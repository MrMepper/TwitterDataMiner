__author__ = 'Chris'

import tweepy
from tweepy import OAuthHandler

#To keep keys secret, left them in a keys.txt file and read them to vars
with open("keys.txt", "r") as f:
    APIlist = []
    for line in f:
        APIlist.append(line)

consumer_key = APIlist[0]
consumer_secret = APIlist[1]
access_token = APIlist[2]
access_secret = APIlist[3]

