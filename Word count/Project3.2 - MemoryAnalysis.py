
from lib.Book import Load, FilterLetters, RemoveStopWords
import lib.WordCounters as Counters
from matplotlib.pyplot import plot, show, bar, xticks, xlabel, ylabel
import numpy as np

bookStringENG = Load("Books/WilliamShakespeareENG.txt")
bookStringFRA = Load("Books/WilliamShakespeareFRA.txt")
bookStringFIN = Load("Books/WilliamShakespeareFIN.txt")
wordsENG = FilterLetters(bookStringENG).split()
wordsFRA = FilterLetters(bookStringFRA).split()
wordsFIN = FilterLetters(bookStringFIN).split()
dataStreamENG = RemoveStopWords(wordsENG, "english")
dataStreamFRA = RemoveStopWords(wordsFRA, "french")
dataStreamFIN = RemoveStopWords(wordsFIN, "finnish")

exactCountENG = Counters.Exact(dataStreamENG)
exactCountFRA = Counters.Exact(dataStreamFRA)
exactCountFIN = Counters.Exact(dataStreamFIN)

(lossyCountENG, entriesENG) = Counters.Lossy(dataStream = dataStreamENG, error = 0.005)
(lossyCountFRA, entriesFRA) = Counters.Lossy(dataStream = dataStreamFRA, error = 0.001)
(lossyCountFIN, entriesFIN) = Counters.Lossy(dataStream = dataStreamFIN, error = 0.001)

lossySortedENG = sorted(lossyCountENG.items(), key=lambda x: x[1], reverse=True)
exactSortedENG = sorted(exactCountENG.items(), key=lambda x: x[1], reverse=True)
lossySortedFRA = sorted(lossyCountFRA.items(), key=lambda x: x[1], reverse=True)
lossySortedFIN = sorted(lossyCountFIN.items(), key=lambda x: x[1], reverse=True)

print()
print()

plot(range(len(dataStreamENG)), entriesENG)
#plot(range(len(dataStreamFRA)), entriesFRA)
#plot(range(len(dataStreamFIN)), entriesFIN)
xlabel("Tamanho da stream")
ylabel("Número de entradas")
show()

print(lossySortedENG[0:15])
print(exactSortedENG[0:15])