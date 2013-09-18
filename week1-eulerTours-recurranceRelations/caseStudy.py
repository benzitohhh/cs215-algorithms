import pdb

import math

def rec_russian(a, b):
    if a == 0: return 0
    if a % 2 == 0: return 2*rec_russian(a/2, b)
    return b + 2*rec_russian((a-1)/2, b)

print rec_russian(4,5)
