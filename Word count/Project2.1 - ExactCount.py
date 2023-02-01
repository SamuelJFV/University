
# Fixed probability counter : 1 / 4 Decreasing probability counter : 1 / 2^k

import lib.Book as book
import lib.Data as data

bookString = book.Load('WilliamShakespeareFRA.txt')
bookString = book.FilterLetters(bookString)

counts = book.ExactCount(bookString)

data.Save("ExactCountsFRA", counts)

print(len(bookString))