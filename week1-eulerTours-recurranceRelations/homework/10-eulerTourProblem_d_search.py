# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
import pdb

def find_eulerian_tour(graph):
    path = find_path(graph, set(), [], graph[0])
    return [edge[0] for edge in path[:-1]] + list(path[-1]) if path else []

def find_path(all_edges, explored, path, current_edge):
    explored = explored | set([current_edge]) | set([tuple(reversed(current_edge))])

    # Note that setA <= setB is true iff setA is a subset of or equal to setB
    if set(all_edges) <= set(explored): return path + [current_edge]

    _, node = current_edge
    successors = [edge for edge in all_edges if node in edge]

    for edge in successors:
        if edge in explored: continue
        edge = edge if node == edge[0] else tuple(reversed(edge))
        result = find_path(all_edges, explored, path + [current_edge], edge)
        if result: return result

    return []

graph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(graph)
