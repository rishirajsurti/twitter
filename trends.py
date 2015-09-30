# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:33:14 2015

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

WORLD_WOE_ID=1
IN_WOE_ID = 23424848
world_trends = t.trends.place(_id=WORLD_WOE_ID)
in_trends = t.trends.place(_id=IN_WOE_ID)

print json.dumps(world_trends,indent=1)
print 
print in_trends

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
in_trends_set = set([trend['name'] for trend in in_trends[0]['trends']])
common_trends = world_trends_set.intersection(in_trends_set)
print common_trends