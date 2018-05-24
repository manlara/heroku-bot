# Dependencies
import tweepy
import json
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets

quote_list = [
    "Quote 11111",
    "Quote 21111",
    "Quote 31111"]

# Create function for tweeting
def QuoteItUp(quote_num):

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully!")

# Set timer to run every minute
counter = 0

while(counter < len(quote_list)):
    QuoteItUp(counter)
    time.sleep(60)
    counter += 1
