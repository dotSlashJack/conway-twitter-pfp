#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update twitter with subsequent game of life runs
@author: jack hester
"""
import tweepy
from datetime import datetime, timedelta, date
from datetime import timedelta
import game_of_life
import os

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
  
# calling the api
api = tweepy.API(auth)

# WARNING: YOU MUST UPDATE d0 WITH THE DATE YOU WANT TO BEGIN UPDATING FROM
d0 = date(2021, 1, 10)
d1 = date.today()

delta = d1 - d0
time = delta.days

# generate files if they don't exist, update prob of being alive in game_of_life.py (under main)
if time < 1:
    # run for 1 year
    game_of_life.main(300, 365)

filename = os.path.join("images", str("game_"+str(time)+".png"))

api.update_profile_image(filename)

print("Your Twitter profile picture was updated")
