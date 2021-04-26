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
    # TODO: check how to choose start
    # Select start vertex as first in adjList
    start = adjList[0]

    # Set initial dist for start as 0
    start.dist = 0

    # Create variable numV to represent number of vertices in graph
	numV = len(adjList)

    # Iterate numV - 1 times
	for n in range(numV - 1):
        # Look at each vertex in graph
        for vertex in adjList:
            # Check each neighbor of vertex
            # Update predictions and previous vertex
            for nbr in vertex.neigh:
                # Create variable length to represent edge weight
                length = adjMat[vertex.rank][nbr.rank]
                # Only update if new value is better than tolerance value
                if nbr.dist > vertex.dist + length + tol:
                    nbr.dist = vertex.dist + length
                    nbr.prev = vertex

    loop = []
    
    # Iterate 1 more time to check for changes indicating arbitrage
    for vertex in adjList:
        for nbr in vertex.neigh:
            # Create variable length to represent edge weight
            length = adjMat[vertex.rank][nbr.rank]
            if nbr.dist > vertex.dist + length + tol:
                nbr.dist = vertex.dist + length
                nbr.prev = vertex
                loop.append(nbr)
                break

    # No negative cost cycle is detected, so return empty list ranks
    if len(loop) == 0:
        return []

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