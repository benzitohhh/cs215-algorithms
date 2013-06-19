
import csv
import heapq
import pprint

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += 1
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += 1        
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    characters = set()
    for (char, book) in tsv:
        make_link(G, char, book)
        characters.add(char)
    return G, characters

G, characters = read_graph("marvel.tsv")

# create graph of  char : {char : weight, ...}
charG = {}
for char1 in characters:
    for book in G[char1]:
        for char2 in G[book]:
            if char1 < char2:
                # avoid double counting
                make_link(charG, char1, char2)

#  heighest (using simple iteration)
heighest = (-1, 'none', 'none')
for char1 in charG:
    for char2 in charG[char1]:
        weight = (charG[char1][char2], char1, char2)
        if weight > heighest:
            heighest = weight
print heighest

# top k (using a heap)
heap=[]
k = 100
for char1 in charG:
    for char2 in charG[char1]:
        if char1 < char2:
            if len(heap) < k:
                heapq.heappush(heap,(charG[char1][char2], (char1, char2)))
            elif charG[char1][char2] > heap[0][0]:
                heapq.heappushpop(heap,(charG[char1][char2], (char1, char2)))
pprint.pprint(sorted(heap))


