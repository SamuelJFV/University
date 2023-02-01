
from itertools import combinations, chain
import numpy as np
import collections

# Test different graphs and different densities
# Report
# References

v = ['A','B','C','D','E','F','G','H']
e = ['AD','CD','CF','GH']
#v = ['A','B','C','D','E','F','G','H']
#eComb = list(combinations(v,2))
#e = [comb[0]+comb[1] for comb in eComb]
#print(e)
graph = {'vertices': v,'edges': e} 

def ValidateMatchings(_combination):
    
    combinationString = ''.join(_combination)
    usedVertices = []

    for vertice in combinationString:
        if vertice in usedVertices:
            return False
        else:
            usedVertices.append(vertice)

    return True

def MaxMatching(_graph):

    vertices = _graph['vertices']
    edges = _graph['edges']

    for i in range(len(e),0,-1):
        
        combinationsList = list(combinations(e,i))
        for combination in combinationsList:
            
            if ValidateMatchings(combination):
                return combination
    return ()

maximumMatching = MaxMatching(graph)
print('The maximum matching is {}, for example the edges: {}'.format(len(maximumMatching),maximumMatching))
