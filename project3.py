"""
Math 560
Project 3
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
	adjList[0].dist = 0
	adjList
	numV = len(adjList)
	for n in range(numV - 1):
        for vertex in adjList:
        	for nbr in vertex.neigh:
                    if nbr.dist > vertex.dist + adjMat[vertex.rank][nbr.rank]):
                    	nbr.dist = vertex.dist + adjMat[vertex.rank][nbr.rank]
                    	nbr.prev = vertex

    return []
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()