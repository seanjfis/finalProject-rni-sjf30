"""
Math 260
Final Project
Spring 2021

Partner 1: Ryan Iki
Partner 2: Sean Fiscus
Date: 04-19-21
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

	numV = len(adjList)
	for n in range(numV - 1):
        for vertex in adjList:
            for nbr in vertex.neigh:
                if nbr.dist > vertex.dist + adjMat[vertex.rank][nbr.rank] + tol:
                    nbr.dist = vertex.dist + adjMat[vertex.rank][nbr.rank]
                    nbr.prev = vertex
    loop = []
    for vertex in adjList:
        for nbr in vertex.neigh:
            if nbr.dist > vertex.dist + adjMat[vertex.rank][nbr.rank] + tol:
                loop.append(nbr)
                break

    i = loop[0].prev

    while i not in loop:
        loop.append(i)
        i = i.prev

    for i in loop:
        if loop[i].isequal(loop[-1]):
            break
        else:
            del loop[i]

    return []

################################################################################

"""
rates2mat
"""

def rates2mat(rates):
    # Return adjacency matrix with correctly weighted edges
    # Edges are weighted as -log(R) where R is the exchange
    # rate between two currencies
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()