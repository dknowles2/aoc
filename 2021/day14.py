#!/usr/bin/python3

from collections import Counter

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read()

ex1 = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def parse(xin):
    arrow = ' -> '
    tmpl = None
    pairs = {}
    for l in xin.strip().split('\n'):
        if not l:
            continue
        if arrow in l:
            pair, ins = l.split(arrow)
            pairs[pair] = ins
        else:
            tmpl = l
    return tmpl, pairs


def one(xin, steps=10, debug=False):
    poly, pairs = parse(xin)
    if debug:
        print(f'Template:      {poly}')

    for s in range(steps):
        new_poly = []
        i = 1
        while i < len(poly):
            p = poly[i-1:i+1]
            new_poly.append(p[0] + pairs.get(p, ''))
            i+=1
        new_poly.append(poly[-1])
        poly = ''.join(new_poly)
        if debug:
            print(f'after step {s+1:2}: {poly[:40]}')
    c = Counter(poly)
    mc = c.most_common()
    print(mc[0][1] - mc[-1][1])


def expand(pairs, pair, remain, depth=5):
    print(pair, remain, depth)
    if depth == 0:
        c = Counter()
        for i in range(len(remain)-1):
            return expand(pairs, remain[i:i+2], remain[i+1:], 0)
            print(remain[i:i+2])
    else:
        return expand(pairs, pair[0]+pairs[pair], pair[1]+remain, depth-1)


def two(xin, steps=10, debug=False):
    poly, pairs = parse(xin)

    c = Counter()
    for i in range(len(poly)-1):
        pair = poly[i:i+2]
        for s in range(steps):
            npair = pair[0] + pairs[pair]
            print(i, pair, s, npair)
            if pair == npair:
                c += Counter(pair)
                pair = npair

    print(c)

    if True:
        return
    if debug:
        print(f'Template:      {poly}')

    c = Counter()
    for s in range(steps):
        new_poly = []
        i = 1
        while i < len(poly):
            p = poly[i-1:i+1]
            print(f'..[{i}] {p} -> {p[0]}{pairs[p]}')
            new_poly.append(p[0] + pairs.get(p, ''))
            i+=1
        new_poly.append(poly[-1])
        poly = ''.join(new_poly)
        print(f'after step {s+1:2}: {poly}')
    c += Counter(poly)
    mc = c.most_common()
    print(mc[0][1] - mc[-1][1])


def solve(xin, steps=10, debug=False):
    poly, pairs = parse(xin)
    if debug:
        print(f'Template:      {poly}')

    poly = list(poly)
    c = Counter()
    for s in range(steps):
        i = 1
        while i < len(poly):
            p = ''.join(poly[i-1:i+1])
            if i == 1 and pairs[p] == p[1]:
                print(f'i={i}; p = {p}; pairs[p] = {pairs[p]}')
                c += Counter(p)
                poly = poly[i:]
                i = 1
                continue
            else:
                poly.insert(i, pairs[p])
                i+=1
            i+=1

        if debug:
            print(f'After step {s+1:2}: {"".join(poly)}')
    c += Counter(poly)
    mc = c.most_common()
    print(mc)
    print(mc[0][1] - mc[-1][1])


one(ex1, steps=10, debug=True)
# solve(ex1, steps=10, debug=True)
# solve(in1, steps=10, debug=True)
print("====two")
two(ex1, steps=4, debug=True)
# solve(in1, steps=20, debug=True)
