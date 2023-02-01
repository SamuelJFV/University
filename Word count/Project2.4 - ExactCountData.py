
import matplotlib.pyplot as plt
import numpy as np
import lib.Data as data
import string

w = .4
countsENG = data.Load("ExactCountsENG")
countsFRA = data.Load("ExactCountsFRA")
countsFIN = data.Load("ExactCountsFIN")

letters = string.ascii_uppercase

names = list(letters)
values1 = list(countsENG.values())
values2 = list(countsFRA.values())
values3 = list(countsFIN.values())

#values2 = list(meanCount.values())
#values2 = [element * 4 for element in values2]

ax = plt.subplot(111)

x = np.arange(len(letters))

ax.bar(x-.2, values1, tick_label=names, width=0.2, color='b', align='center', label='Inglês')
ax.bar(x, values2, tick_label=names, width=0.2, color='g', align='center', label='Francês')
ax.bar(x+.2, values3, tick_label=names, width=0.2, color='r', align='center', label='Filandês')
plt.xlabel("Letras")
plt.ylabel("Número de occorrências")
plt.legend()
plt.show()

#Sort to make the Exact count Tables (tab I e tab II)
countsDict = countsENG
countsDict = {k: v for k, v in sorted(countsDict.items(), key=lambda item: item[1])}
print(countsDict)
countList = list(countsDict.values())
countPerc = [100*count/sum(countList) for count in countList]
print(countPerc)