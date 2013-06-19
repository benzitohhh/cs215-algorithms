#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
#
# Hint: you need to find the median!

def partition(seq):
    pi, seq = seq[0], seq[1:]   # pick and remove the pivot
                                # i.e. could also randomly pick the pivot index here...
    smaller = [x for x in seq if x <= pi] # all the small elements
    bigger = [x for x in seq if x > pi]   # all the large ones
    return smaller, pi, bigger            # pi is "in the right place"

def select(seq, k):
    """
    find the kth smallest element,
    where k is in range(len(seq))
    """
    smaller, pi, bigger = partition(seq)
    m = len(smaller)
    if m == k: return pi
    elif m < k:
        return select(bigger, k-m-1)
    else:
        return select(smaller, k)

def find_median(L):
    return select(L, len(L)/2)

def minimize_absolute(L):
    return find_median(L)

L = [1,2,3]
print minimize_absolute(L)
