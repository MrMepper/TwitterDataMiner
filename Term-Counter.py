__author__ = 'Chris'


import operator
import json
from collections import Counter
import Tokenizer
from nltk.corpus import stopwords
from nltk import download
import string

download()
fname = input("Enter file name")
token = Tokenizer

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

#Finds most common strings(words) from dictionary of tweets.
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_all = [term for term in token.preprocess(tweet['text']) if term not in stop]
        count_all.update(terms_all)
    print(count_all.most_common(5))

