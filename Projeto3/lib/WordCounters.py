
from math import ceil


def Exact(dataStream : list):

    """Returns a dictionary with the exact count of each word from a given string"""

    counts = {}

    for word in dataStream:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts
        
def Lossy(dataStream: list, error: float):

    """
    Returns a tuple where in the index: \n
    0: contains a dictionary with the count of each word from a given string using a lossy counter algorithm.\n
    1: contains the total number of entries for each iteration of the lossy counter algorithm.

    """
    
    entries = {}

    currentLenght = 1
    bucketId = 1
    bucketWidth = 1/error
    numberOfEntries = [None]*len(dataStream)
    
    for word in dataStream:

        if word in entries:
            entries[word][0] += 1

        else: 
            entries[word] = [1, bucketId-1]

        if currentLenght%bucketWidth == 0:
            
            bucketId = currentLenght/bucketWidth
            oldEntries = entries.copy()
            
            for word in oldEntries:
                 
                count = oldEntries[word][0]
                delta = bucketId-oldEntries[word][1]
                
                if count <= delta:
                    del entries[word]

        numberOfEntries[currentLenght-1] = len(entries)
        currentLenght += 1

    return entries, numberOfEntries
    #return {word: entries[word] for word in entries if entries[word][0] >= (support-error)*currentLenght}, numberOfEntries
