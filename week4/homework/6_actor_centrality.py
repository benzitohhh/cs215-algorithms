import fileinput


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




G = {}
actors = set()
movies = set()
fi = fileinput.input(['/Users/immanuel_ben/Desktop/cs215-algorithms/week4/homework/imdb-1.tsv'])
for line in fi:
    line = line.rstrip('\n')
    actor, movie, year = line.split("\t")
    make_link(G, actor, movie)
    actors.add(actor)
    movies.add(movie)
fi.close()
actors = list(actors)
movies = list(movies)

avg_centrality_per_actor = {}
for actor in actors:
    avg_centrality_per_actor[actor] = centrality_average(G, actor)

# TODO: BEN: shouldn't this be the min here?
res = sorted(avg_centrality_per_actor, key = lambda x: avg_centrality_per_actor[x])
