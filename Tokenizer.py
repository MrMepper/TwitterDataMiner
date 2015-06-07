__author__ = 'Chris'

from nltk.tokenize import word_tokenize
import re
import json

#Two lists that hold Regular Expressions

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

#Add to re compiler
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

#Insert data to be searched, returns a list of matches.
def tokenize(s):
    return tokens_re.findall(s)

#Takes in data to be searched, converts to lowercase if true
def preprocess(s, lowercase=False):
    #Calls and runs tokenize function, which returns a list of all matches
    tokens = tokenize(s)
    if lowercase:
        #Iterates through list, converts to lowercase if it is not an emoticon
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

#Test Code
if __name__ == '__main__':
    with open('python.json', 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            print(tokens)

