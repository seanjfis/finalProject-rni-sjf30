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
    # Select start vertex as first in adjList
    # Set initial dist for start as 0
    #TODO: initialize values as inf (distance) and None (neighbors)
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
    adjList[0].dist = 0

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

    # Create empty list to store vertices that are in negative cost cycle
    changed = []
    
    # Iterate 1 more time to check for changes indicating arbitrage
    for vertex in adjList:
        for nbr in vertex.neigh:
            # Create variable length to represent edge weight
            length = adjMat[vertex.rank][nbr.rank]
            if nbr.dist > vertex.dist + length + tol:
                nbr.dist = vertex.dist + length
                nbr.prev = vertex
                changed.append(nbr)


    # If changed list is empty, no negative cost cycle was detected
    # Return empty list for ranks
    if len(changed) == 0:
        return []

    # If changed list is not empty, there is a negative cost cycle
    # Set u to be the previous vertex to the vertex whose value changed
    # in the final iteration
    u = changed[0].prev
    loop = []
    loop.append(changed[0]) #TODO: add additional code comments

    # Trace backwards and add vertices to loop list to close the cycle
    # While previous vertex is not already in the loop, append that vertex
    # and look at the next previous vertex
    while u not in loop:
        loop.append(u)
        u = u.prev

    # While loop stopped executing, meaning u is already present in the loop
    # Append final vertex to loop list to close the cycle
    loop.append(u)

    # Remove vertices that are not part of cycle by removing first vertex
    # in loop until starting and ending vertices are the same
    # while not loop[0].isEqual(loop[-1]):
        #loop.pop(0)
        #TODO: make more efficient by finding index of start and slicing
    end = loop[-1]
    startInd = loop.index(end)
    loop = loop[startInd:]

    # Create empty ranks list to store the rank of each vertex in cycle
    ranks = []

    # Iterate backwards through loop list and append the rank of each
    # vertex to create ranks list with cycle in the correct order
    for i in range(len(loop) - 1, -1, -1):
        ranks.append(loop[i].rank)

    # Return list ranks corresponding to the negative cost cycle
    return ranks

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