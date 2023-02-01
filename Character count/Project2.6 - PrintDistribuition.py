
import matplotlib.pyplot as plt
import numpy as np
import lib.Data as data
import lib.Statitics as statitics
import string

w = .4

distribuitionsENG = data.Load("DistribuitionsMorrisENG")
distribuitionsFRA = data.Load("DistribuitionsMorrisFRA")
distribuitionsFIN = data.Load("DistribuitionsMorrisFRA")

distribuition = distribuitionsENG['E']

plt.xlabel("Número de eventos contados")
plt.ylabel("Número de repetições de cada evento")

plt.hist(distribuition)
plt.show()