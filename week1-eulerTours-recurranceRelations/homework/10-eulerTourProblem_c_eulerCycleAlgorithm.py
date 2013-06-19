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

def find_eulerian_tour(graph):
    E = graph[:]                   # copy the graph so we don't destroy it
    tour = []                      # the tour starts out empty

    def find_tour(u):              # define find_tour as a closure to avoid global variables
        for (i, j) in E:           # find an edge with u as the source node
            if i == u:             # check each edge going one way
                E.remove((i, j))   # remove the found edge so it isn't used twice
                find_tour(j)       # continue the tour from the sink node
            elif j == u:           # check each edge going the other way if we need to
                E.remove((i, j))
                find_tour(i)
        tour.append(u)             # we found an edge from u, so its part of the tour

    find_tour(E[0][0])             # find a tour using the first node in the edge list
    tour.reverse()                 # reverse the node list since it was built backwards

    return tour




# Yeah, typically you don't ever want to modify an iterator... and most libraries for many languages won't let you. The only reason I did it here is because the element being removed is the element that was just used, so its in no risk of being referenced later on. This is because the graph representation is a list of edges, and in a Euler circuit you can only cross each edge once and only once.

# The reason for append instead of insert(0, u) has to do with memory allocation. Typically (and this isn't always true, depending on the underlying structure), when you insert at the head of an array you have to allocate more space and then copy all existing data and move it, where as at the end of an array you just have to allocate more space. I forget if python uses linked lists or arrays for their lists since its based on either C or Java, depending on implementation. Either way, reverse is fast for this application and uses no real memory since its destructive.
