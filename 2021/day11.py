#!/usr/bin/python3

from collections import deque
import itertools

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.readlines()

ex = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip().split("\n")


def parse(xin):
    ret = {}
    for y, l in enumerate(xin):
        for x, e in enumerate(l.strip()):
            ret[(x, y)] = int(e)
    return ret


def get_adj(octos, x, y):
    return [o for o in [(x, y-1), (x, y+1),
                        (x-1, y), (x+1, y),
                        (x-1, y-1), (x-1, y+1),
                        (x+1, y-1), (x+1, y+1)]
            if o in octos]


def step(xin, octos):
    flashed = set()
    to_inc = deque(octos.keys())
    while to_inc:
        o = to_inc.popleft()
        octos[o] += 1
        if octos[o] == 10:
            flashed.add(o)
            for a in get_adj(octos, *o):
                if octos[a] < 10:
                    to_inc.append(a)
    for o in flashed:
        octos[o] = 0

    return len(flashed)


def num_flashes(xin, steps=100):
    octos = parse(xin)
    f = 0
    for s in range(steps):
        f += step(xin, octos)
    print(f)


def first_sync(xin):
    octos = parse(xin)
    for s in itertools.count(1):
        if len(octos) == step(xin, octos):
            print(s)
            return

num_flashes(ex, steps=100)
num_flashes(in1, steps=100)
print("====two")
first_sync(ex)
first_sync(in1)
