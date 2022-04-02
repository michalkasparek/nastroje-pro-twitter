#!/usr/bin/env python

import tweepy

client = tweepy.Client(bearer_token="") # sem přijde autorizační Bearer Token

ja = "" # vaše uživatelské jméno
prvni = "" # u. j. prvního uživatele
druhy = "" # u. j. druhého uživatele

ja_id = client.get_user(username=ja)
ja_id = ja_id.data.id
prvni_id = client.get_user(username=prvni)
prvni_id = prvni_id.data.id
druhy_id = client.get_user(username=druhy)
druhy_id = druhy_id.data.id

users = client.get_users_following(id=ja_id, max_results=1000, user_fields=["protected"])
sleduju = set()
for user in users.data:
    if user.protected == False:
        try:
            sleduju.add(user.username)
        except:
            pass

users = client.get_users_following(id=prvni_id, max_results=1000, user_fields=["protected"])
sleduje1 = set()
for user in users.data:
    chraneny = user.protected
    if chraneny == False:
        try:
            sleduje1.add(user.username)
        except:
            pass


users = client.get_users_following(id=druhy_id, max_results=1000, user_fields=["protected"])
sleduje2 = set()
for user in users.data:
    chraneny = user.protected
    if chraneny == False:
        try:
            sleduje2.add(user.username)
        except:
            pass

sledujioba = set()
sledujioba = set.intersection(sleduje1, sleduje2)

mamsledovat = set()
mamsledovat = sledujioba.difference(sleduju)

for x in mamsledovat:
    print("https://twitter.com/" + x)