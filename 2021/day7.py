#!/usr/bin/python3

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = list(map(int, f.read().split(',')))

ex = list(map(int, "16,1,2,0,4,2,7,1,2,14".split(',')))


import collections


def align(xin, cost=lambda a, i, n: abs(i - a) * n):
    c = collections.Counter(xin)
    fuels = []
    for a in range(min(xin), max(xin)):
        f = 0
        for i, n in c.most_common():
            if a == i:
                continue

            f += cost(a, i, n)
        fuels.append((a, f))
    print(min(fuels, key=lambda x: x[1]))



align(list(ex))
align(in1)

print('===two')
def cost2(a, i, n):
    x = abs(a-i)
    return int((x**2+x)/2)*n

align(ex, cost=cost2)
align(in1, cost=cost2)
