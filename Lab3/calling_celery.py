from tasks import get_lines, count_pronouns, count_in_file
from celery import group
import time
import os

# celery worker -A tasks --loglevel=INFO -n worker1@%h --autoscale=10,3
# sudo pkill -9 -f 'celery worker'
def add_dicts(dicts):
    dd = {}
    for d in dicts:
        for key, value in d.items():
            if not key in dd: dd[key] = value
            dd[key] = dd[key] + value
    return dd


def main():
    directory = '/home/ubuntu/ACC-Labs/Lab3/data'
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]
    print("3 workers")
    times = []
    for i in range(5):
        job = []
        for filename in os.listdir(directory):
            job.append(count_in_file.delay(directory + os.sep + filename, p))
        #job_result = job.apply_async()
        start = time.time()
        #job_result = count_pronouns(dir)
        #print the result
        results = []
        for job_result in job:
            results.append(job_result.get())
            #print(results) 
        print(add_dicts(results))
        end = time.time()-start
        times.append(end)
        print(end)
    print(times)


main()
