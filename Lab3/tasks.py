from celery import Celery, group, chord
import os
import json
import re
import time

broker_url = 'amqp://tabea:tabeapassword@localhost:5672/tabeavhost'
app = Celery('tasks', backend='rpc://', broker=broker_url )
@app.task
def add_dicts(dicts):
    dd = {}
    for d in dicts:
        for key, value in d.items():
            if not key in dd: dd[key] = value
            dd[key] = dd[key] + value
    return dd


@app.task
def count_in_file(filename, p):
    start = time.time()
    pron_count = {key: 0 for key in p}
    with open(filename) as tweet_file:
        tweets = (line.rstrip() for line in tweet_file)
        tweets_json = (json.loads(line) for line in tweets if line)

        for tweet in tweets_json:
            # only consider non retweets
            if "retweeted_status" not in tweet:
                words = re.split('[. , ? !]', tweet['text'])
                for w in words: 
                    if w.lower() in p: # if the word is a pronoun, add it to the count
                        pron_count[w.lower()] += 1
    return [time.time()-start, pron_count]
