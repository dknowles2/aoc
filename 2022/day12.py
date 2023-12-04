#!/usr/bin/python3

from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from pathlib import Path
import sys


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


@dataclass(order=True)
class Item:

    p: int
    k: tuple


def one(inp):
    graph = {}
    pend = []
    pidx = {}
    dist = {}

    start, end = None, None
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            k = (x, y)
            graph[k] = {"S": 0, "E": 25}.get(c, ord(c) - ord("a"))
            dist[k] = 0 if c == "S" else 1e7
            pidx[k] = Item(dist[k], k)
            heappush(pend, pidx[k])
            if c == "S":
                start = k
            if c == "E":
                end = k

    def adj(n):
        nx, ny = n
        keys = [(nx-x, ny-y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]]
        return [k for k in keys if k in graph]

    while pend:
        cur = heappop(pend)
        for n in adj(cur.k):
            if graph[n] - graph[cur.k] > 1:
                continue
            alt = dist[cur.k] + 1
            if alt  < dist[n]:
                dist[n] = alt
                pidx[n].p = alt
                heapify(pend)
        if cur == end:
            break

    print(dist[end])



def two(inp):
    graph = {}
    pend = []
    pidx = {}
    dist = {}

    start, end = None, None
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            k = (x, y)
            graph[k] = {"S": 0, "E": 25}.get(c, ord(c) - ord("a"))
            dist[k] = 0 if c == "E" else 1e7
            pidx[k] = Item(dist[k], k)
            heappush(pend, pidx[k])
            if c == "S":
                start = k
            if c == "E":
                end = k

    def adj(n):
        nx, ny = n
        keys = [(nx-x, ny-y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]]
        return [k for k in keys if k in graph]

    while pend:
        cur = heappop(pend)
        for n in adj(cur.k):
            if graph[n] - graph[cur.k] < -1:
                continue
            #if graph[n] - graph[cur.k] > 1:
            #    continue
            alt = dist[cur.k] + 1
            if alt  < dist[n]:
                dist[n] = alt
                pidx[n].p = alt
                heapify(pend)
        if cur == start:
            break

    print(dist[end])


ex = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()

one(ex)
two(ex)
