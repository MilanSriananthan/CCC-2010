comps = int(input())
all = []
names = []
value = []
top = []
low =[]
if comps > 0:

    for i in range(comps):
        new = input()
        hold = new.split(" ")
        names.append(hold[0])
        all.append(hold)
    if comps == 1:
        print(all[0][0])
    else:

        def score(seq):
            return 2*int(seq[1]) + 3*int(seq[2]) + int(seq[3])

        for i in range(comps):
            value.append(score(all[i]))
        high = value.count(max(value))
        if value.count(max(value)) > 1:
            high = value.count(max(value))
            for i in range(high):
                here = value.index(max(value))
                top.append(names[here])
                names.remove(names[here])
                value.remove(max(value))
        else:
            top.append(names[value.index(max(value))])
            names.remove(names[value.index(max(value))])
            value.remove(max(value))

            high = value.count(max(value))
            if value.count(max(value)) > 1:
                high = value.count(max(value))
                for i in range(high):
                    here = value.index(max(value))
                    low.append(names[here])
                    names.remove(names[here])
                    value.remove(max(value))
            else:
                low.append(names[value.index(max(value))])
                value.remove(max(value))

        top.sort()
        low.sort()
        final = top + low
        print(final[0])
        print(final[1])



'''

5
ABC 20 20 20
DEF 10 20 30
GHI 11 2 2
ZZZ 20 20 20
JKL 20 20 20



1
ABC 20 20 20
'''