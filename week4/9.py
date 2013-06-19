# List of node centrality values from example graph
L = [2, 3, 4, 3, 2, 4]

def mean(L):
    total = 0
    for i in L:
        total += i
    return (0.0 + total) / len(L)
print mean(L)
