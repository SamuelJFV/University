
from lib.Book import Load, FilterLetters, RemoveStopWords
import lib.WordCounters as Counters
from matplotlib.pyplot import plot, show, bar, xticks, xlabel, ylabel
import numpy as np

bookString = Load("Books/WilliamShakespeareENG.txt")
words = FilterLetters(bookString).split()
dataStream = RemoveStopWords(words, "english")

exactCount = Counters.Exact(dataStream)
(lossyCount, entries) = Counters.Lossy(dataStream = dataStream, error = 0.005)

exactSorted = sorted(exactCount.items(), key=lambda x: x[1], reverse=True)
lossySorted = sorted(lossyCount.items(), key=lambda x: x[1], reverse=True)

print()
print()
counts = exactSorted[0:15]
countsLossy = []

for wordCount in lossySorted[0:15]:
    countsLossy.append((wordCount[0],wordCount[1][0]))

print(countsLossy)
print(counts)
bar(range(len(counts)), [val[1] for val in counts], align='center')
bar(range(len(countsLossy)), [val[1] for val in countsLossy], align='center')
xticks(range(len(counts)), [val[0] for val in counts])
xticks(rotation=30)
ylabel("Counts")

show()