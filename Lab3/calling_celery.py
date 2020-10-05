from tasks import get_lines, count_pronouns, count_in_file
from celery import group
import time
import os
def add_dicts(dicts):
    dd = {}
    for d in dicts:
        for key, value in d.items():
            if not key in dd: dd[key] = value
            dd[key] = dd[key] + value
    return dd


def main():
    directory = '/home/ubuntu/ACC-Labs/Lab3/datatest'
    p = ["den", "det", "denna", "denne","han", "hon",  "hen"]
    job = group(count_in_file.s(directory + os.sep + filename, p) for filename in os.listdir(directory))
    job_result = job.apply_async()
    start = time.time()
    #job_result = count_pronouns(dir)
    #print the result
    results = job_result.get()
    print(results) 
    print(add_dicts(results))
    print(time.time()-start)


main()