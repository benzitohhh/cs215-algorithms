import csv
import time
import heapq

filename = '/Users/immanuel_ben/Desktop/learn/cs215-algorithms/week4/homework/imdb-1.tsv'

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def centrality_average(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current]:
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return (0.0 + sum(distance_from_start.values())) / len(distance_from_start)

def heap_search(k, big_array):
    # to compare the items, create a class
    class ResObj(list):
        def __lt__(self, other):
            return self[1] < other[1]
    return heapq.nsmallest(k, [ResObj(i) for i in big_array])

G = {}
actors = set()
movies = set()

tsv = csv.reader(open(filename), delimiter='\t')
for (actor, movie_name, year) in tsv:
    # ensure movie names are unique by appending year
    movie = str(movie_name) + ", " + str(year)
    make_link(G, actor, movie)
    actors.add(actor)
    movies.add(movie)

actors = list(actors)
movies = list(movies)

avg_centrality_per_actor = {}
for actor in actors:
    avg_centrality_per_actor[actor] = centrality_average(G, actor)

# if n is relatively small, this is ok:
#res = sorted(avg_centrality_per_actor.items(), key = lambda x: x[1])
#res = res[:20]

# But if n is large, use a heap to keep track of n smallest
res = heap_search(20, avg_centrality_per_actor)

print res
