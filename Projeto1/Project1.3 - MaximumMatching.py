
from lib.GraphFile import Graph
from itertools import combinations, chain
import pickle
import time

n = 80
data = {'maxMatching':[],'time':[],'vertices':[],'edges':[],'solutionsTested':[],'numBasicOperations':[]}

def MaxMatchingExhaustiveV1(graph):

    global solutionsTested
    global numBasicOperations
    
    m = graph.m
    n = graph.n
    matrix = graph.matrix
    maxConnections = [0]*n
    solution = None
    
    edgesSets = chain.from_iterable([combinations(range(m),i+1) for i in range(m)])
    
    for edgesSet in edgesSets:
        solutionsTested += 1
        connectedVertices = [0]*n
        for edge in edgesSet:
            connectedVertices += matrix[edge]
            numBasicOperations += 1
        isMatching = all([connection <= 1 for connection in connectedVertices])
        numBasicOperations += len(connectedVertices)
        isBetterSolution = sum(connectedVertices) > sum(maxConnections)
        numBasicOperations += 1
        if isMatching and isBetterSolution:
            maxConnections = connectedVertices
            solution = edgesSet
    return solution

def MaxMatchingExhaustiveV2(graph):

    global solutionsTested
    global numBasicOperations
    
    m = graph.m
    n = graph.n
    matrix = graph.matrix
    
    edgesSets = chain.from_iterable([combinations(range(m),i+1) for i in range(m-1,-1,-1)])
    
    for edgesSet in edgesSets:
        solutionsTested += 1
        connectedVertices = [0]*n
        for edge in edgesSet:
            connectedVertices += matrix[edge]
            numBasicOperations += 1
        isMatching = all([connection <= 1 for connection in connectedVertices])
        numBasicOperations += len(connectedVertices)
        if isMatching:
            return edgesSet
        
def MaximumMatchingGreedy(graph):

    global solutionsTested
    global numBasicOperations
    
    m = graph.m
    n = graph.n
    matrix = graph.matrix
    solutionSet = []
    connectedVertices = [0]*n
    
    for i in range(m):
        solutionsTested += 1
        connectedVertices += matrix[i]
        numBasicOperations += 1
        isMatching = all([connection <= 1 for connection in connectedVertices])
        numBasicOperations += len(connectedVertices)
        
        if isMatching:
            solutionSet.append(i)
        else:
            connectedVertices -= matrix[i]
            numBasicOperations += 1
            
    return solutionSet


for i in range(3,n+1):
    solutionsTested = 0
    numBasicOperations = 0
    graph = Graph.Load('graph{}'.format(i))
    graph.DelIsolated()
    start = time.time()

    #maxMatching = MaxMatchingExhaustiveV1(graph)
    #maxMatching = MaxMatchingExhaustiveV2(graph)
    maxMatching = MaximumMatchingGreedy(graph)
    
    end = time.time()
    deltaTime = end - start

    print(i)
    
    data['maxMatching'].append(len(maxMatching))
    data['time'].append(deltaTime)
    data['vertices'].append(graph.n)
    data['edges'].append(graph.m)
    data['solutionsTested'].append(solutionsTested)
    data['numBasicOperations'].append(numBasicOperations)

#filename = 'dataExhaustiveV1'
#filename = 'dataExhaustiveV2'
filename = 'dataGreedy'
outfile = open('Data/'+filename,'wb')
pickle.dump(data,outfile)
outfile.close()
