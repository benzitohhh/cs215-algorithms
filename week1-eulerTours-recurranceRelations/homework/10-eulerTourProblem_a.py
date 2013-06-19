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

import unittest

def find_eulerian_tour(graph):
    # your code here
    for x, y in graph:
        frontier = [(x, y)]     # ordered list of paths we have blazed
        while frontier:
            path = frontier.pop()
            # are all the edges visited in this path?
            # And are first and last nodes the same?
            # Then return it, we're done!

            # for each possible successor to path,
            # create a new path and add it to frontier

    return Fail

def is_tour(path):
    return True

def all_edges_visited(path, graph):
    return False

def get_successors():
    return True


class TestEuler(unittest.TestCase):
    def setUp(self):
        # triangle
        self.graph1 = [(1, 2), (2, 3), (3, 1)]
        # triangle of triangles
        self.graph2 = [
                        (1, 2),
                        (1, 5),
                        (2, 3),
                        (2, 3),
                        (2, 4),
                        (2, 5),
                        (3, 4),
                        (4, 5),
                        (4, 6),
                        (5 ,6),
        ]

    def test_all_edges_visited(self):
        graph1_pathsg_complete = [
            [(1, 2), (2, 3), (3, 1)],
            [(3, 1), (1, 2), (2, 3)]
        ]
        graph1_pathsg_missing = [
            []              ,
            [(3, 1)]        ,
            [(3, 1), (2, 3)],
            [(3, 1), (1, 2)],
            [(1, 2), (2, 3)],
        ]

        for p in graph1_pathsg_complete:
            self.assertTrue(all_edges_visited(p, self.graph1))

        for p in graph1_pathsg_missing:
            self.assertFalse(all_edges_visited(p, self.graph1))

    def test_get_successors(self):
        graph1_path_expsuc_list = [
            #path,                     expsuc,
            [(1, 2)],                  set([(2, 3)]),
            [(2, 3)],                  set([(3, 1)]),
            [(1, 2), (2, 3)],          set([(3, 1)]),
            [(1, 2), (2, 3), (3, 1)],  set([])      ,
            [(3, 1)],                  set([(1, 2)]),
            [(2, 3), (3, 1), (1, 2)],  set([])      ,
        ]
        graph2_path_expsuc_list = [
            #path,                     expsuc,
            [(1, 2)],                  set([(2, 3), (2, 4)]),
            [(1, 5)],                  set([(2, 5), (4, 5)]),
            [(1, 2), (2, 3)],          set([(3, 4)]),
            [(1, 2)],                  set([(2, 3), (2, 4)]),
        ]


unittest.main()
