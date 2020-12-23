import math
houses = int(input())
all = []
for i in range(houses):
    hold = int(input())
    all.append(hold)

hydrents = int(input())
all.sort()

def farthest(seq):
    length = 0
    if len(seq) > 1:
        length = (seq[-1] - seq[0]) /2
    if length > 500000:
        length = 1000000 - length
    return length

def other(seq):
    length = 0
    if len(seq) > 1:
        length = seq[-1] - seq[0]
    if length > 500000:
        length = 1000000 - length
    return length

def difference(seq):
    lower = []
    higher = []
    maxdiff = (seq[-1] + seq[0])/2
    for i in seq:
        if i <= maxdiff:
            lower.append(i)
        else:
            higher.append(i)
    return [lower, higher]
all = [all]

for i in range(hydrents-1):
    divide = all
    longest = 0
    for x in divide:
        if other(x) > longest:
            longest = other(x)
            hold = x
    all.remove(hold)
    control = difference(hold)
    all.append(control[0])
    all.append(control[1])

great = 0
for i in all:
    if farthest(i) > great:
        great = farthest(i)
        check = i
print(math.ceil(great))
'''
9
10
0
1000
2000
3400
545
134
4500
20000
4



'''