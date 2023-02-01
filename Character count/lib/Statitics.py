
from math import log 

def Mean(values : list):
    return sum(values)/len(values)

def ExpectedValue(n: float, p: float):        
        
    return n*p

def ExpectedValueMorris(n: float):

    return log(n+1)/log(2)


def StandartDeviation(values : list, p : float, algoritm : str = 'simple'):

    if algoritm == 'simple':
        return (ExpectedValue(values)*p)**.5
    elif algoritm == 'morris':
        return None
    return None

def AbsoluteError(value, exactValue):
    return abs(value - exactValue)

def RelativeError(value, exactValue):
    return AbsoluteError(value,exactValue)/exactValue