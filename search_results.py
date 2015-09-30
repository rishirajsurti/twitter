# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:51:23 2015

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

q = '#inspire'
count=10

search_results = t.search.tweets(q=q, count=count)
statuses = search_results['statuses']

for _ in range(5):
    print "Lenght of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e:
        break;
    
    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
    search_results = t.search.tweets(**kwargs)
    statuses+=search_results['statuses']

print json.dumps(statuses[0],indent=1)