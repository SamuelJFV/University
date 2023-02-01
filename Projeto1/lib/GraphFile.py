
from random import randint, seed
import numpy as np
from matplotlib.pyplot import scatter, plot, text, xlim, ylim, show
import pickle

class Graph:
    
    def __init__(self, mecNumber = randint(0,99999), n = 4, m = 4, length = 9):

        self.length = length
        self.n = n
        self.m = m
        self.seed = mecNumber
        seed(mecNumber)
                
        matrix = [[0 for i in range(n)] for j in range(m)]
        verticesCoordinates = []
        edgesCoordinates = []

        while len(verticesCoordinates) < n:
            coordinates = [randint(1,self.length), randint(1,self.length)]
            
            if coordinates not in verticesCoordinates:
                verticesCoordinates.append(coordinates)

        i = 0
        while len(edgesCoordinates) < m:
            idx0 = randint(0,n-1)
            idx1 = randint(0,n-1)
            coordinates = [verticesCoordinates[idx0], verticesCoordinates[idx1]]
            
            if idx0 != idx1:
                matrix[i][idx0] = 1
                matrix[i][idx1] = 1
                
                if matrix[i] not in matrix[:i]:
                    edgesCoordinates.append(coordinates)
                    i += 1
                    
                else:
                    matrix[i] = [0]*n

        self.matrix = np.array(matrix)
        self.verticesCoordinates = np.array(verticesCoordinates)
        self.edgesCoordinates = np.array(edgesCoordinates)
        
        
    def Show(self, edges = []):
        
        scatter(self.verticesCoordinates[:,0],self.verticesCoordinates[:,1],color="black")
        [plot(self.edgesCoordinates[i,:,0],self.edgesCoordinates[i,:,1],color="lightgray") for i in range(self.m)]
        [plot(self.edgesCoordinates[edge,:,0],self.edgesCoordinates[edge,:,1],'--') for edge in edges]
        [text(self.verticesCoordinates[i,0],self.verticesCoordinates[i,1],str(i),color="blue") for i in range(self.n)]
        [text((self.edgesCoordinates[i,0,0]+self.edgesCoordinates[i,1,0])/2,(self.edgesCoordinates[i,0,1]+self.edgesCoordinates[i,1,1])/2,str(i),color="red") for i in range(self.m)]
        xlim(0,self.length+1)
        ylim(0,self.length+1)
        show()

    def DelIsolated(self):

        seed(self.seed)
        matrix = self.matrix
        n = self.n
        
        for i in range(self.n):            
            while not any(matrix.transpose()[i]):
                newEdge = [0]*n
                idx = randint(0,n-1)
                if idx != i:
                    newEdge[i] = 1
                    newEdge[idx] = 1
                    coordinates = [self.verticesCoordinates[i], self.verticesCoordinates[idx]]
                    self.edgesCoordinates = np.append(self.edgesCoordinates,np.array([coordinates]),axis = 0)
                    matrix = np.append(matrix, np.array([newEdge]), axis = 0)

        self.matrix = matrix
        self.m = len(matrix)
        
    def Save(self, filename):
        
        with open('GraphObjects/'+filename, 'wb') as outp:
            pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)

    def Load(filename):
        
        inputFile = open('GraphObjects/'+filename, 'rb')
        loadedGraph = pickle.load(inputFile)
        inputFile.close()
        return loadedGraph
