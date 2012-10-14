# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    return (0.5 * n) * (n + 1) + 2

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j


for i in range(10):
    print count(i), clique(i)
