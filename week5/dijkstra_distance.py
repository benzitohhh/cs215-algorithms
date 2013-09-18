def dijkstra(G,v):
    "Given a starting node v, find distance to all the other nodes"
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    # NOTE: the below loop will only work with connected graphs
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

def shortest_dist_node(dist_so_far):
    return min(dist_so_far, key = dist_so_far.get)
