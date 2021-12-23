#!/usr/bin/python3

from collections import namedtuple
import heapq
from itertools import product
import os


def get_input():
    return os.path.join(
        os.path.dirname(__file__),
        "input",
        os.path.basename(__file__).replace(".py", ".txt"))


with open(get_input()) as f:
    in1 = f.read()


ex1 = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

Point = namedtuple("Point", ["x", "y"])


def parse1(xin):
    risks = {}
    for y, l in enumerate(xin.strip().split()):
        for x, r in enumerate(l):
            risks[Point(x, y)] = int(r)
    return risks


def parse2(xin):
    risks = parse1(xin)
    w, h = max(risks).x+1, max(risks).y+1
    erisks = {}
    for p, r in risks.items():
        for i in range(5):
            for j in range(5):
                inc = i + j
                nr = 1 + (r + inc - 1) % 9
                np = Point(p.x+i*w, p.y+j*h)
                erisks[np] = nr
    return erisks


class MinHeap:

    def __init__(self):
        self.S = set()
        self.Q = []

    def __contains__(self, i):
        return i in self.S

    def __len__(self):
        return len(self.Q)

    def push(self, i, p):
        self.S.add(i)
        heapq.heappush(self.Q, (p, i))

    def pop(self):
        _, i = heapq.heappop(self.Q)
        self.S.remove(i)
        return i


def min_risk_astar(risks):
    src = Point(0, 0)
    dst = max(risks.keys())
    h = lambda p: (dst.x - p.x) + (dst.y - p.y)
    d = lambda p: risks[p]  # distance is risk level
    get_neighbors = lambda p: [
        n for n in
        [Point(p.x+1, p.y), Point(p.x-1, p.y),
         Point(p.x, p.y+1), Point(p.x, p.y-1)]
        if n in risks
    ]

    inf = float("inf")
    open_set = MinHeap()
    open_set.push(src, inf)

    prev = {}
    g_score = {p: inf for p in risks}
    g_score[src] = 0

    f_score = {p: inf for p in risks}
    f_score[src] = h(src)

    while open_set:
        cur = open_set.pop()
        if cur == dst:
            path = [dst]
            while cur in prev:
                cur = prev[cur]
                if cur != src:
                    path.append(cur)
            return sum(d(p) for p in path)

        for n in get_neighbors(cur):
            t_g_score = g_score[cur] + d(n)
            if t_g_score < g_score[n]:
                prev[n] = cur
                g_score[n] = t_g_score
                f_score[n] = t_g_score + h(n)
                if n not in open_set:
                    open_set.push(n, g_score[n])
    raise ValueError


print(min_risk_astar(parse1(ex1)))
print(min_risk_astar(parse1(in1)))
print("===two")
print(min_risk_astar(parse2(ex1)))
print(min_risk_astar(parse2(in1)))
