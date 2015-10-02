# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:36:35 2015

@author: rishiraj
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:38:56 2015

@author: rishiraj
"""

#%%
import twitter
import json

def load_credentials():
    cred=[];
    for line in open('twitter.txt','r').read().splitlines():
        cred.append(line);
    global CONSUMER_KEY;
    global CONSUMER_SECRET;
    global OAUTH_TOKEN;
    global OAUTH_TOKEN_SECRET;
    CONSUMER_KEY = cred[0]
    CONSUMER_SECRET = cred[1];
    OAUTH_TOKEN = cred[2];
    OAUTH_TOKEN_SECRET = cred[3]    

load_credentials();
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET  )
t = twitter.Twitter(auth=auth)

#query
q = raw_input("Enter search query:");
count=100;

search_results = t.search.tweets(q=q, count=count)
statuses = search_results['statuses']

status_texts = [ status['text'] for status in statuses]
screen_names = [ user_mention['screen_name']
                for status in statuses
                    for user_mention in status['entities']['user_mentions']] 
hashtags = [ hashtag['text'] for status in statuses
                for hashtag in status['entities']['hashtags']]
                
words = [w for tt in status_texts
            for w in tt.split()]

print json.dumps(status_texts[0:5], indent=1)                        
print json.dumps(screen_names[0:5], indent=1)                        
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent = 1)