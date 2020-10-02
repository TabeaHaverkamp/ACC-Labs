
import matplotlib.pyplot as plt
execution_time = {}
execution_time['1'] = 
for key,vals in execution_time.items():
    avg[key] = mean(vals)


plt.plot(*zip(*avg.items()),  c='red', label = 'average execution time')
plt.plot(*zip(*execution_time.items()), '+', c='grey')
plt.ylabel("seconds")
plt.xlabel("file")
plt.title("to Volume")
plt.savefig()
plt.show()

