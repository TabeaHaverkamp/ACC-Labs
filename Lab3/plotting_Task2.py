
import matplotlib.pyplot as plt
from statistics import mean

ex_time_onevm = {}
ex_time_onevm['1'] =  [35.37020134925842,
                        36.876641511917114,
                        40.19391894340515,
                        38.883694648742676,
                        37.741069078445435]
ex_time_onevm['2'] = [49.1056067943573, 
                        45.6214873790741, 
                        51.690048933029175, 
                        47.37272882461548, 
                        47.967658281326294]

ex_time_onevm['3'] = [56.5629346370697, 56.30590510368347, 61.633443117141724, 60.689159631729126, 55.53092551231384]
avg = {}
for key,vals in ex_time_onevm.items():
    avg[key] = mean(vals)


ex_time = {}

ex_time['3'] = [107.86399292945862, 106.49290800094604, 107.8594696521759, 97.92719960212708, 102.66747426986694]
ex_time['7'] = [103.4112069606781,98.1205005645752,99.53335642814636,102.6190447807312,105.04641652107239] 
plt.plot(*zip(*avg.items()),  c='red', label = 'average execution time')
plt.plot(*zip(*ex_time_onevm.items()), '+', c='grey')
plt.ylabel("seconds")
plt.xlabel("amount of workers")
plt.title("Time counting swedish pronouns")
plt.savefig("images/counter_3workers_1vm.png")
plt.show()

