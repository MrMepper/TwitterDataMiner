# TwitterDataMiner
Data Miner for Twitter

Various tools I use to get data from Twitter.
##Files
----------------------------
getposts.py - Accesses twitter API and streams posts from a twitter page.  
Listener.py - Listener Object that takes in Stream Listener, used in getposts.py  
organize-data.py - Input filename, organizes the data based on JSON dict-value.  
Organizer.py - Organizer Object used  in organize-data.py. Uses JSON to load string and format.  
Token.py - Needs to be an Object, creates common tokens used in Twitter and compiles them into RE.  
Term-Counter.py - Counts terms in 'text' from JSON


##Project Plans
The purpose of this project has moved over to RedditBot, Twitter has found to not be "personal" enough to enable correlations between negative keywords and programming languages.  
For now this will just serve as a reference to various Twitter tools I used to gather information.
