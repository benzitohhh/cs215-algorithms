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

# This solution uses a search approach.
# It is not the most efficient way of doing this,
# as it will repeat certain checks.

def find_eulerian_tour(graph):
    frontier = [[graph[0]]]
    paths_of_node = find_successors(graph)
    while frontier:
        path = frontier.pop(0)
        if is_eulerian_tour(path, graph):
            return nodes_of_path(path)
        for edge in paths_of_node[path[-1][-1]]:
            if edge not in path and reverse(edge) not in path:
                frontier.append(path + [edge])
    return []

def find_successors(graph):
    result = {}
    for edge in graph:
        result[edge[0]] = result.get(edge[0], [])
        result[edge[1]] = result.get(edge[1], [])
        result[edge[0]].append(edge)
        result[edge[1]].append(reverse(edge))
    return result

def is_eulerian_tour(path, graph):
    if len(set(path)) != len(set(graph)) or path[0][0] != path[-1][-1]:
        return False
    for i in range(len(graph)-1):
        if path[i][-1] != path[i+1][0]:
            return False
    return True

def reverse(edge):
    a,b = edge
    return b,a

def nodes_of_path(path):
    return  [a for a,b in path] + [path[0][0]]

graph = [(0, 1), (1,2),(2,0)]
print find_eulerian_tour(graph)
graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print find_successors(graph)
print find_eulerian_tour(graph)
