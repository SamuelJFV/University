
from lib.GraphFile import Graph
from random import seed, randint

n = 20
numMec = 89055
seed(numMec)

for i in range(3,n+1):
    numEdges = randint(i,min(i+5,i*(i-1)/2))
    #numEdges = int(i*(i-1)/2)
    graph = Graph(numMec,i,numEdges)
    graph.Save('graph{}'.format(i))
