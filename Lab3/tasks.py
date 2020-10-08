from celery import Celery, group, chord
import os
import json
import re
import time

broker_url = 'amqp://tabea:tabeapassword@localhost:5672/tabeavhost'
app = Celery('tasks', backend='rpc://', broker=broker_url )



@app.task
def count_in_file(filename, p):
    pron_count = {key: 0 for key in p}
    tweet_file = open(filename)

    tweets = (line.rstrip() for line in tweet_file)
    tweets_json = (json.loads(line) for line in tweets if line)

    for tweet in tweets_json:
        # only consider non retweets
        if "retweeted_status" not in tweet:
            words = re.split('[. , ? !]', tweet['text'])
            for w in words: 
                if w.lower() in p: # if the word is a pronoun, add it to the count
                    pron_count[w.lower()] += 1
    return pron_count
