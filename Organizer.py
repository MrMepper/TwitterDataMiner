__author__ = 'Chris'

import json


class Organizer(object):

    filename = ""

    def __init__(self, filename):
        self.filename = filename

    def organize(self):
        with open (self.filename, "r") as f:
            line = f.readline()
            tweet = json.loads(line)
            print(json.dumps(tweet, indent = 4))