# TwitterDataMiner
Data Miner for Twitter

Various tools I use to get data from Twitter.

getposts.py - Accesses twitter API and streams posts from a twitter page
Listener.py - Listener Object that takes in Stream Listener, used in getposts.py
organize-data.py - Input filename, organizes the data based on JSON dict-value.
Organizer.py - Organizer Object used  in organize-data.py. Uses JSON to load string and format.
Token.py - Needs to be an Object, creates common tokens used in Twitter and implements them into RE