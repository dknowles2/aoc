#!/usr/bin/python3

from collections import defaultdict as ddict
import os

def get_input():
    return os.path.join(
        os.path.dirname(__file__),
        "input",
        os.path.basename(__file__).replace(".py", ".txt"))


with open(get_input()) as f:
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
    rules = {}
    for l in xin.strip().split('\n'):
        if not l:
            continue
        if arrow in l:
            pair, ins = l.split(arrow)
            rules[pair] = ins
        else:
            tmpl = l
    return tmpl, rules


def solve(xin, steps=10, debug=False):
    tmpl, rules = parse(xin)
    if debug:
        print(f'Template:      {tmpl}')

    def grow(pairs, rules):
        new_pairs = ddict(int)
        for p, c in pairs.items():
            ins = rules[p]
            new_pairs[p[0]+ins] += c
            new_pairs[ins+p[1]] += c
        return new_pairs

    pairs = ddict(int)
    for i in range(len(tmpl)-1):
        pairs[tmpl[i]+tmpl[i+1]] += 1

    for s in range(steps):
        pairs = grow(pairs, rules)
        if debug:
            print(f"after step {s+1:2}: {1+sum(pairs.values())}")

    ltrs = ddict(int, {tmpl[0]: 1, tmpl[-1]: 1})
    for p, c in pairs.items():
        ltrs[p[0]] += c
        ltrs[p[1]] += c

    most = 0
    least = float('inf')
    for v in ltrs.values():
        most = max(most, v)
        least = min(least, v)
    print(int((most - least) / 2))


smart(in1, steps=10)
smart(in1, steps=40)
