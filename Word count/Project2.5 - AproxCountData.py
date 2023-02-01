
import matplotlib.pyplot as plt
import numpy as np
import lib.Data as data
import lib.Statitics as statitics
import string

w = .4
p = 1/4
countsENG = data.Load("ExactCountsENG")
countsFRA = data.Load("ExactCountsFRA")
countsFIN = data.Load("ExactCountsFIN")
distribuitionsENG = data.Load("DistribuitionsENG")
distribuitionsFRA = data.Load("DistribuitionsFRA")
distribuitionsFIN = data.Load("DistribuitionsFIN")
distribuitionsMorrisENG = data.Load("DistribuitionsMorrisENG")
distribuitionsMorrisFRA = data.Load("DistribuitionsMorrisFRA")
distribuitionsMorrisFIN = data.Load("DistribuitionsMorrisFIN")


letters = string.ascii_uppercase
meanCountENG =  {letter: 0 for letter in letters}
meanCountFRA =  {letter: 0 for letter in letters}
meanCountFIN =  {letter: 0 for letter in letters}
meanCount =  {letter: 0 for letter in letters}
meanCountMorris =  {letter: 0 for letter in letters}
counts = countsENG

for letter in letters:
    meanCount[letter] = statitics.Mean(distribuitionsENG[letter])/p
    meanCountMorris[letter] = (2**statitics.Mean(distribuitionsMorrisENG[letter]))-1

names = list(letters)
values1 = list(counts.values())
values2 = list(meanCount.values())
values3 = list(meanCountMorris.values())

#values2 = list(meanCount.values())
#values2 = [element * 4 for element in values2]

ax = plt.subplot(111)

x = np.arange(len(letters))

ax.bar(x-.2, values1, tick_label=names, width=0.2, color='b', align='center', label='Contagem exata')
ax.bar(x, values2, tick_label=names, width=0.2, color='g', align='center', label='Contagem com probabilidade fixa')
ax.bar(x+.2, values3, tick_label=names, width=0.2, color='r', align='center', label='Contagem com probabilidade decrescente')
plt.xlabel("Letras")
plt.ylabel("Número de occorrências contadas/estimadas")
plt.legend()
plt.show()