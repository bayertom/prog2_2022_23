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

def BFS(G, u, P):
    # All nodes are new
    S = ['N'] * (len(G) + 1)

    # Create queue
    Q = []

    # Add starting node and change status
    Q.append(u)
    S[u] = 'O'

    # Until Q is empty
    while Q:
        # Take fist node
        u = Q.pop(0)

        # Browse its neighbors
        for v in G[u]:

            #Node is new
            if S[v] == 'N':
                # Change its status
                S[v] = 'O'

                # Remember itd predecessor
                P[v] = u

                # Add v to Q
                Q.append(v)

        # U is closed
        S[u] = 'C'


def recPath(u, v, P):
    #Reconstruct path u-v backward
    path = []

    # Repeat unit we reach u
    while v != u and v != None:
        path.append(v)
        v = P[v]

    path.append(v)

    return path

p = [-1] * (len(G)+1)
BFS(G, 1, p)

print(p)

path = recPath(1, 9, p)
print(path)