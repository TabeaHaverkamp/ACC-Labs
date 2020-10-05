from tasks import get_lines, count_pronouns
from celery import group
import time

dir = '/home/ubuntu/ACC-Labs/Lab3/data'
# build groups to be executed
#g = [get_lines.s('/home/ubuntu/ACC-Labs/Lab3/data') for x in range(5)]
#job = group(g)

#execute the group
# job_result = job()
job_result = count_pronouns.delay(dir)
#print the result
results = job_result.get() 
print(results)