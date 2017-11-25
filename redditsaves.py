import easygui
import requests
import json
import praw
import sys

msg = "Enter reddit credentials"
title = "Reddit Save Manager"
fieldNames = ["Username", "Password"]
fieldValues = easygui.multpasswordbox(msg, title, fieldNames)

# Store credentials to use for authentication
redditUser = fieldValues[0]
redditPass = fieldValues[1]

reddit = praw.Reddit(client_id='i1-7kia6OKVzjA',
                        client_secret='fub3y0voA-IKuX4nEwkPfUqHbC8',
                        user_agent='redditsavemanager by /u/redditsavemanager',
                        password=redditPass,
                        username=redditUser)

if( reddit.user.me() != redditUser ):
    sys.exit()

savedLinks = reddit.user.me().saved().__iter__()
while True:
    try:
        print(savedLinks.next())
    except StopIteration as e:
        break
