from tasks import get_lines
import time
t = []
for i in range(10):
    start = time.time()
    print(get_lines('/home/ubuntu/ACC-Labs/Lab3/data'))
    t.append(time.time() - start)

print(t)