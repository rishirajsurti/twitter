# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:31:15 2015

@author: rishiraj
"""
#%%
import twitter
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
twitter_api = twitter.Twitter(auth=auth)

print twitter_api
