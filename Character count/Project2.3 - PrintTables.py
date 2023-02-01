

import lib.Data as data
import lib.Statitics as statistics
import string

p = 1/4
d = 2
counts = data.Load('ExactCountsFIN')
distribuitions = data.Load('DistribuitionsMorrisFIN')
#distribuitions = data.Load('DistribuitionsFIN')
#tableLetters = ['E','A','T','O','S']
tableLetters = list(string.ascii_uppercase)

print()
#TABELA 1
#print('  Counts  média Estimação')
#TABELA 2
#print('  Valor médio Valor min Valor max')

for letter in tableLetters:

    count = counts[letter]
    distribuition = distribuitions[letter]

    letters = string.ascii_uppercase
    #expectedValue = statistics.ExpectedValueMorris(count)
    expectedValue = statistics.ExpectedValue(count,p)
    meanEvents = statistics.Mean(distribuition)
    estimative = (2**meanEvents)-1
    lowestValue = (2**min(distribuition))-1
    highestValue = (2**max(distribuition))-1
    #estimative = meanEvents/p
    #lowestValue = min(distribuition)/p
    #highestValue = max(distribuition)/p


    if count == 0:
        absError = {'expected':'-','lowest':'-','highest':'-'}
        relError = {'expected':'-','lowest':'-','highest':'-'}
    else:
        absError = {
            'expected': statistics.AbsoluteError(estimative,count),
            'lowest': statistics.AbsoluteError(lowestValue,count),
            'highest': statistics.AbsoluteError(highestValue,count)}

        relError = {
            'expected': statistics.RelativeError(estimative,count),
            'lowest': statistics.RelativeError(lowestValue,count),
            'highest': statistics.RelativeError(highestValue,count)}
    #TABLE 1
    #print('{0} & {1:.{4}f} & {2:.{4}f} & {3:.{4}f}'.format(letter,count,meanEvents,estimative,d)+r' \\)
    #TABLE 2
    #print('{0} & {1:.{4}f}\% & {2:.{4}f}\% & {3:.{4}f}\%'.format(letter,100*relError['expected'],100*relError['lowest'],100*relError['highest'],d)+r' \\)
    #TABLE ANEXOS
    if count == 0:
        print('{0} & {1:.{11}f} & {2:.{11}f} & {3:.{11}f} & {4:.{11}f} & - & -'.format(letter,count,estimative,expectedValue,meanEvents,100*relError['expected'],100*relError['lowest'],100*relError['highest'],absError['expected'],absError['lowest'],absError['highest'],d)+r' \\')
    else:
        print('{0} & {1:.{11}f} & {2:.{11}f} & {3:.{11}f} & {4:.{11}f} & {5:.{11}f}\% / {6:.{11}f}\% / {7:.{11}f}\% & {8:.{11}f} / {9:.{11}f} / {10:.{11}f}'.format(letter,count,estimative,expectedValue,meanEvents,100*relError['expected'],100*relError['lowest'],100*relError['highest'],absError['expected'],absError['lowest'],absError['highest'],d)+r' \\')
