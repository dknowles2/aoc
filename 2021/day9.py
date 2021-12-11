#!/usr/bin/python3

from functools import reduce
from operator import mul

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read().split('\n')

ex = """\
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip().split('\n')

def parse(xin):
    ret = {}
    for y, l in enumerate(xin):
        for x, v in enumerate(l):
            ret[(x, y)] = int(v)
    return ret


def get_adj(pts, x, y):
    return [pt for pt in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] if pt in pts]


def is_lowest(pts, x, y):
    for adj in get_adj(pts, x, y):
        if pts[(x, y)] >= pts[adj]:
            return False
    return True


def find_lows(pts):
    lows = []
    for (x, y), h in pts.items():
        if is_lowest(pts, x, y):
            lows.append((x, y))
    return lows


def get_basin(pts, x, y):
    basin = {(x, y)}
    for pt in get_adj(pts, x, y):
        if pts[pt] < 9 and pts[pt] > pts[(x, y)]:
            basin.update(get_basin(pts, *pt))
    return basin


def part_one(xin):
    pts = parse(xin)
    lows = [pts[pt] for pt in find_lows(pts)]
    print(sum(lows) + len(lows))


def part_two(xin):
    pts = parse(xin)
    basins = [get_basin(pts, *l) for l in find_lows(pts)]
    basin_sizes = sorted([len(b) for b in basins], reverse=True)
    print(reduce(mul, basin_sizes[:3]))


part_one(ex)
part_one(in1)
print("===two")
part_two(ex)
part_two(in1)
