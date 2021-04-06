import tweepy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import csv

from resources.const import *


def get_tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = api.user_timeline(screen_name=userID, count=200, include_rts = False, tweet_mode = 'extended')

    all_tweets = []
    all_tweets.extend(tweets)
    oldest_id = tweets[-1].id
    while True:
        tweets = api.user_timeline(screen_name=userID, count=200, include_rts = False, max_id = oldest_id - 1, tweet_mode = 'extended')
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)
        print('N of tweets downloaded till now {}'.format(len(all_tweets)))
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8").decode("utf-8")] for idx,tweet in enumerate(all_tweets)]
    df_tweets = pd.DataFrame(outtweets,columns=["id","created_at", "text"])
    
    return  df_tweets
