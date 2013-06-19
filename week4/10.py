# List of node centrality values from example graph
L = [2, 3, 4, 3, 975, 4]

def max(L):
    m = L[0]
    for i in L:
        if i > m: m = i
    return m

print max(L)
