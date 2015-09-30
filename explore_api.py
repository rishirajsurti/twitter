# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:35:24 2015

@author: rishiraj
"""

#%%

import twitter
from twitter import *
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

t.statuses.home_timeline()
t.statuses.user_timeline(screen_name="rogerfederer")

for i in xrange(10):
    st = "Automatically generated tweet number: "+str(i);
    t.statuses.update(status=st);
    
t.search.tweets(q='#inspire')

x = t.statuses.home_timeline()
x[0]['user']['screen_name']


img=[];
   
for i in range(1,5):
    with open("coast"+str(i)+".jpg","rb") as imagefile:
        imagedata = imagefile.read()
    t_up = Twitter(domain='upload.twitter.com',
                   auth=auth);
    img.append(t_up.media.upload(media=imagedata)["media_id_string"])


t.statuses.update(status="Auto attached.", media_ids=img[0]);


###random tweets
import random
import string

digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
print digits + chars