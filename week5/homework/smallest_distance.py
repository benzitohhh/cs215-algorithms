#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
#

import heapq

def dijkstra(G,v):
    result, queue, heap = {}, {v:0}, [(0, v)]

    while queue:
        weight, head = heapq.heappop(heap)
        if head in result or (head in queue and queue[head] < weight):
            continue
        result[head] = weight
        del queue[head]

        for successor in G[head]:
            if successor not in result:
                new_weight = result[head] + G[head][successor]
                if successor not in queue or new_weight < queue[successor]:
                    heapq.heappush(heap, (new_weight, successor))
                    queue[successor] = new_weight
    return result

############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)

    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)
    return dist

d = test()
