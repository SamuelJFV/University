
import pickle
import matplotlib.pyplot as plt
import pandas as pd

filename = 'Data\dataExhaustiveV1'
inputFile = open(filename,'rb')
data = pickle.load(inputFile)
inputFile.close()


xData = data['time']
yData = data['maxMatching']
for i in range(len(xData)):
    print(xData[i],end = ' ')
print()
print()
for i in range(len(xData)):
    print(yData[i],end = ' ')
    
