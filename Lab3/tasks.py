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
def count_pronouns(directory):
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]
    pron_count = {key: 0 for key in p}
    for filename in os.listdir(directory):
        with open(directory + os.sep + filename, "r") as file:
            Lines = file.readlines() 
            files_group = chord(group([count_in_line.s(line, p) for line in Lines])(), add_dicts.s()) 
            


@app.task
def count_in_line(line, p):
    pron_count = {key: 0 for key in p}
    if line.strip(): # do not consider empty lines  
        # get the line as json file
        j = json.loads(line)
        # only consider non retweets
        if "retweeted_status" not in j:
            words = re.split('[. , ? !]', j['text'])
            for w in words: 
                if w.lower() in p: # if the word is a pronoun, add it to the count
                    pron_count[w.lower()] += 1
    return pron_count


@app.task
def get_lines(directory):
    start = time.time()
    # create a dictionary to store the result
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]
    pron_count = {key: 0 for key in p}
    for filename in os.listdir(directory):
        with open(directory + os.sep + filename, "r") as file:
            Lines = file.readlines() 
            for line in Lines:
                if line.strip(): # do not consider empty lines  
                    # get the line as json file
                    j = json.loads(line)
                    # only consider non retweets
                    if "retweeted_status" not in j:
                        words = re.split('[. , ? !]', j['text'])
                        for w in words: 
                            if w.lower() in p: # if the word is a pronoun, add it to the count
                                pron_count[w.lower()] += 1
    return json.dumps(pron_count, sort_keys=True), time.time()-start



