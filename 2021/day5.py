#!/usr/bin/python3

import collections

with open("input/" + __file__.replace(".py", ".txt")) as f:
    input1 = f.readlines()

ex = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

def parse(xin):
    ret = []
    for l in xin:
        p1, p2 = l.split(" -> ")
        ret.append((tuple(map(int, p1.split(","))),
                    tuple(map(int, p2.split(",")))))
    return ret

def p(mx, my, counts):
    mx, my = 9, 9
    for y in range(0, my+1):
        for x in range(0, mx+1):
            print(counts.get((x, y), "."), end="")
        print()
    print()

def solve(xin, diag=False, debug=False):
    segments = parse(xin)
    counts = collections.defaultdict(int)
    mx, my = 0, 0
    for p1, p2 in segments:
        if debug:
            print(p1, "-->", p2)
        (x1, y1), (x2, y2) = p1, p2
        mx = max(x1, x2, mx)
        my = max(y1, y2, my)
        if x1 != x2 and y1 != y2:
            if not diag:
                continue
            seg = []
            xmod = 1 if x1 < x2 else -1
            ymod = 1 if y1 < y2 else -1
            for x, y in zip(range(x1, x2+xmod, xmod),
                            range(y1, y2+ymod, ymod)):
                seg.append((x, y))
        elif x1 == x2:
            seg = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)]
        elif y1 == y2:
            seg = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]

        for x, y in seg:
            counts[(x, y)] += 1
        if debug:
            p(mx, my, counts)
    ttl = sum(1 for c in counts.values() if c > 1)
    print(ttl)

def one(xin, debug=False):
    solve(xin, diag=False, debug=debug)

def two(xin, debug=False):
    solve(xin, diag=True, debug=debug)

print("=== one")
one(ex)
one(input1)

print()
print("=== two")
two(ex)
two(input1)
