
# Fixed probability counter : 1 / 4 Decreasing probability counter : 1 / 2^k

import lib.Book as book
import lib.Data as data
import string

bookString = book.Load('WilliamShakespeareENG.txt')
bookString = book.FilterLetters(bookString)

nTimes = 100
p = 0.5

letters = string.ascii_uppercase
distribuitions =  {letter: [0]*nTimes for letter in letters}

def powInt(n,p):

    if p == 0:
        return 1

    return powInt(n,p-1)*n

for i in range(nTimes):
    
    for letter in bookString:

        #distribuitions[letter][i] += book.IncrementCount(p)

        count = distribuitions[letter][i]
        distribuitions[letter][i] += book.IncrementCount(powInt(p,count))

#data.Save("DistribuitionsENG", distribuitions)
data.Save("DistribuitionsMorrisENG", distribuitions)