#!/usr/bin/env python

import tweepy

client = tweepy.Client(bearer_token="") # sem přijde autorizační Bearer Token

uzivatelske_jmeno = "" # vaše (nebo cizí…) uživatelské jméno

id = client.get_user(username=uzivatelske_jmeno)
id = id.data.id

users = client.get_users_following(id=id, max_results=1000, user_fields=["protected"])

for user in users.data:
    chraneny = user.protected
    if chraneny == False:
        try:
            tweets_list = client.get_users_tweets(user.id, exclude="retweets", tweet_fields=["created_at"])
            for x in tweets_list.data[:1]:
                datum = x.created_at
                print(str(user.username) + ";" + str(datum))
        except:
            pass