from tasks import get_lines, count_pronouns
from celery import group
import time
def add_dicts(dicts):
    dd = {}
    for d in dicts:
        for key, value in d.items():
            if not key in dd: dd[key] = value
            dd[key] = dd[key] + value
    return dd
dir = '/home/ubuntu/ACC-Labs/Lab3/data'

start = time.time()
job_result = count_pronouns(dir)
#print the result
results = job_result.get()
print(results) 
#print(add_dicts(results))
print(start-time.time())