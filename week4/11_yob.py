# Read in file
f = open('yob.txt')
names = []
for line in f:
    s = line.replace("\n","").split(",")
    names.append([int(s[2]), s[0], s[1]])

names = sorted([n for n in names if n[2]=='F'])

print names[-2]
