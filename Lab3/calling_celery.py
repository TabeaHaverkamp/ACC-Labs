from tasks import get_lines
import celery
import time
t = []

def on_raw_message(body):
    print(body)
# [get_lines('/home/ubuntu/ACC-Labs/Lab3/data') for x in range(5)]
job = celery.group([get_lines('/home/ubuntu/ACC-Labs/Lab3/data'), get_lines('/home/ubuntu/ACC-Labs/Lab3/data')])
start = time.time()
job_result = job.delay()
results = job_result.get() # this will block until the tasks finish but it wont deadlock
print(time.time()-start)
