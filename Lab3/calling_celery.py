from tasks import count_in_file#, add_dicts
from celery import group
import time
import os

# celery -A tasks worker --loglevel=INFO -n worker1@%h --autoscale=10,3 --max-memory-per-child 100
# sudo pkill -9 -f 'celery worker'
def add_dicts(dicts):
    dd = {}
    for d in dicts:
        for key, value in d.items():
            if not key in dd: dd[key] = value
            dd[key] = dd[key] + value
    return dd


def main():
    directory = '/mnt/tweet_data/tweet_data'
    #directory = '/home/ubuntu/ACC-Labs/Lab3/data'
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]
    #print("3 workers")
    times = []
    itimes = []
    for i in range(5):
        job = []
        for filename in os.listdir(directory):
            job.append(count_in_file.delay(directory + os.sep + filename, p))
        #job_result = job.apply_async()
        start = time.time()

        results = []
        individual_times = []
        for job_result in job:
            jb = job_result.get()
            print(jb)
            results.append(jb[1])
            individual_times.append(jb[0])

        #print(time.time()- start)
        print(f" sume of individual times added up: {sum(individual_times)}")
        print(add_dicts(results))
        end = time.time()-start
        times.append(end)
        itimes.appen(sum(individual_times))
        #print(end)
    print(times)
    print(itimes)

main()