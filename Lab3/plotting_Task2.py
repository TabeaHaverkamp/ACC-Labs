
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


#plt.plot(*zip(*avg.items()),  c='red', label = 'average execution time')
#plt.plot(*zip(*ex_time_onevm.items()), '+', c='grey')
#plt.ylabel("seconds")
#plt.xlabel("amount of workers")
#plt.title("Time counting swedish pronouns")
#plt.savefig("images/counter_3workers_1vm.png")
#plt.show()




ex_time = {}
#ex_time['3'] = [107.86399292945862, 106.49290800094604, 107.8594696521759, 97.92719960212708, 102.66747426986694]

ex_time['1'] = [57.882837772369385, 59.98159122467041, 61.729454040527344, 58.69568133354187, 58.683106660842896]
ex_time['2'] = [55.429163455963135, 57.82354426383972, 55.16939902305603, 53.21920919418335, 56.315134048461914]
ex_time['3'] = [48.00873684883118, 54.707953453063965, 46.587767601013184, 60.34901762008667, 56.920199155807495]
ex_time['4'] = [54.46466279029846, 55.33811020851135, 53.68162989616394, 56.48856210708618, 53.734517097473145]
ex_time['5'] = [56.83455944061279, 57.34813737869263, 63.2933886051178, 67.42712020874023, 61.57888436317444]
ex_time['6'] = [67.31468629837036, 67.8301317691803, 66.70208168029785, 72.25498986244202, 69.17902421951294]
ex_time['7'] = [103.4112069606781,98.1205005645752,99.53335642814636,102.6190447807312,105.04641652107239] 
#ex_time['7']= [101.25492310523987, 80.88575387001038, 92.35317468643188, 84.09365391731262, 78.57831978797913]

avg2 = {}
for key,vals in ex_time.items():
    avg2[key] = mean(vals)


plt.plot(*zip(*avg2.items()),  c='red', label = 'average execution time')
plt.plot(*zip(*ex_time.items()), '+', c='grey')
plt.ylabel("seconds")
plt.xlabel("amount of workers")
plt.title("Time counting swedish pronouns")
plt.savefig("images/counter_7workers_7vm.png")
plt.show()
