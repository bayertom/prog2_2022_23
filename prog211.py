import queue
from math import *

#Graph
G = {
    1 : [2, 3, 5],
    2 : [1, 3, 4, 7, 8],
    3 : [1, 2, 6, 7],
    4 : [2, 9],
    5 : [1, 6],
    6 : [3, 5, 7, 8, 9],
    7 : [2, 3, 6, 8],
    8 : [2, 6, 7, 9],
    9 : [4, 6, 8]
}

#Graph with weights
G2 = {
    1 : {2:8, 3:4, 5:2},
    2 : {1:8, 3:5, 4:2, 7:6, 8:7},
    3 : {1:4, 2:5, 6:3, 7:4},
    4 : {2:2, 9:3},
    5 : {1:2, 6:5},
    6 : {3:3, 5:5, 7:5, 8:7, 9:10},
    7 : {2:6, 3:4, 6:5, 8:3},
    8 : {2:7, 6:7, 7:3, 9:1},
    9 : {4:3, 6:10, 8:1}
}

def DFS(G, u, P):
    #Depth first search
    S = ['N'] * (len(G)+1)
    DFSR(G, S, P, u)

def DFSR(G, S, P, u):
    #Depth first search, recursive procedure
    S[u] = 'O'

    # Browse its neighbors
    for v in G[u]:
        # Node is new
        if S[v] == 'N':
            # Remember itd predecessor
            P[v] = u

            #Recursion
            DFSR (G, S, P, v)

    #Close the node
    S[u] = 'C'


def DFSS(G, u, P):
    # All nodes are new
    S = ['N'] * (len(G) + 1)

    #Create stack
    ST = []

    # Add start vertex to stack
    ST.append(u)

    S[u] = 'O'

    #While stack not empty
    while ST:
        # Take fist node
        u = ST.pop()

        # Change its status
        S[u] = 'O'

        # Browse its neighbors in revered order
        for v in reversed(G[u]):

            #Node is new
            if S[v] == 'N':

                # Remember its predecessor
                P[v] = u

                # Add v to Q
                ST.append(v)

        #Close node
        S[u] = 'C'


def recPath(u, v, P):
    # Reconstruct path u-v backward
    path = []

    # Repeat unit we reach u
    while v != u and v != None:
        path.append(v)
        v = P[v]

    path.append(v)

    return path

def dijkstra(G, P, s, e):
    d = [inf] * (len(G) + 1)

    # Priority queue
    PQ = queue.PriorityQueue()

    # Add starting node
    PQ.put((0, s))
    d[s] = 0

    # Until PQ is empty
    while not PQ.empty():
        # Get node with the lowest priority
        du, u = PQ.get()

        # Browse its neighbors
        for v, wuv in G[u].items():
            # Relax
            if d[v] > d[u] + wuv:
                d[v] = d[u] + wuv
                P[v] = u

                # Add v to PQ
                PQ.put((d[v], v))
    return d[e]

#DFS, recursive
P = [None] * (len(G)+1)
DFS(G, 2, P)
print(P)
path = recPath(1, 4, P)
print(path)

P2 = [None] * (len(G)+1)
DFSS(G, 1, P2)
print(P2)
path = recPath(1, 4, P2)
print(path)

#DFS, stack
P3 = [None] * (len(G)+1)
DFSS(G, 1, P3)
print(P3)
path = recPath(1, 4, P3)
print(path)

#Dijkstra
P = [None] * (len(G2)+1)
#dist = dijkstra(G2, P, 1, 9)
#path = recPath(1, 9, P)
#print(path)
#print(dist)
