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
q = '#inspire'
count=100

search_results = t.search.tweets(q=q, count=count)
statuses = search_results['statuses']

f = open('tweets.txt','w');

for i in xrange(count):
    print(statuses[i]['text']);
    f.write((statuses[i]['text']).encode('utf-8')) ;
    f.write("\n\n")    
    print();
f.close();

print encode('utf02')