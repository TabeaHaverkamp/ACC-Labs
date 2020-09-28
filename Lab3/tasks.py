from celery import Celery
import os
import json
import re

broker_url = 'amqp://tabea:tabeapassword@localhost:5672/tabeavhost'
#app = Celery('tasks', broker='broker_url')
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def get_lines(directory):
    # create a dictionary to store the result
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]# "bajs", "trump", "sverige"]
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
                            w = w.lower()
                            if w in p: # if the word is a pronoun, add it to the count
                                pron_count[w] += 1
    import matplotlib.pyplot as plt # needs to be installed in cloudinit
    plt.bar(range(len(pron_count)), list(pron_count.values()), align='center')
    plt.xticks(range(len(pron_count)), list(pron_count.keys()))
    plt.savefig(directory + "plot")
    plt.show()
    return pron_count    



            