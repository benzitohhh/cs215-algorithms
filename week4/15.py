L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36]

def rank(L, v):
    pos = 0
    for val in L:
        if val < v: pos += 1
    return pos


# Returns a partially sorted list
# where all values prior to v are less than v,
# and vice versa
# This is called a partition

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller.append(val)
        if val > v: bigger.append(val)
    return smaller + [v] + bigger

partition(L, 84)
