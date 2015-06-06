__author__ = 'Chris'


import operator
import json
from collections import Counter
import Tokenizer

fname = input("Enter file name")
token = Tokenizer

with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_all = [term for term in token.preprocess(tweet)]
        count_all.update(terms_all)
    print(count_all.most_common(5))

