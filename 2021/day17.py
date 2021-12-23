#!/usr/bin/python3

from dataclasses import dataclass
from itertools import product
import os
import re


def get_input():
    return os.path.join(
        os.path.dirname(__file__),
        "input",
        os.path.basename(__file__).replace(".py", ".txt"))


with open(get_input()) as f:
    in1 = f.read()


ex1 = "target area: x=20..30, y=-10..-5\n"


@dataclass
class Point:
    x: int
    y: int


def parse(xin):
    pattern = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
    match = re.match(pattern, xin.strip())
    if not match:
        raise ValueError(f"Unpraseable input: {xin}")
    g = match.groups()
    return (Point(int(g[0]), int(g[2])), Point(int(g[1]), int(g[3])))


def step(p, v):
    p = Point(p.x + v.x, p.y + v.y)
    v = Point(v.x, v.y)  # copy
    if v.x > 0:
        v.x -= 1
    elif v.x < 0:
        v.x += 1
    v.y -= 1
    return p, v


def in_target(p, t):
    return (
        p.x >= t[0].x and p.x <= t[1].x and
        p.y >= t[0].y and p.y <= t[1].y)


def target_delta(p, t):
    td = Point(0, 0)
    if p.x >= t[0].x and p.x <= t[1].x:
        td.x = 0
    elif p.x < t[0].x:
        td.x = p.x - t[0].x
    else:
        td.x = p.x - t[1].x

    if p.y >= t[0].y and p.y <= t[1].y:
        td.y = 0
    elif p.y < t[0].y:
        td.y = p.y - t[0].y
    else:
        td.y = p.y - t[1].y

    return td


def test_velocity(v, t):
    p = Point(0, 0)
    my = 0
    while True:
        p, v = step(p, v)
        my = max(my, p.y)
        td = target_delta(p, t)
        if td == Point(0, 0):
            return True, my
        if td.x > 0 or td.y < 0:
            return False, None
    return False, None


def one(t):
    max_v = None
    max_h = None
    for x, y in product(range(200), repeat=2):
        v = Point(x, y)
        hit, mvh = test_velocity(v, t)
        if hit and (max_h is None or mvh > max_h):
            max_v = v
            max_h = mvh

    return max_v, max_h



def two(t):
    num_hits = 0
    for x, y in product(range(-200, 400), repeat=2):
        v = Point(x, y)
        hit, _ = test_velocity(v, t)
        if hit:
            num_hits += 1
    return num_hits


t_ex = parse(ex1)
t_in = parse(in1)
# assert test_velocity(Point(7, 2), t_ex) == (True, 3)
# assert test_velocity(Point(6, 3), t_ex) == (True, 6)
# assert test_velocity(Point(9, 0), t_ex) == (True, 0)
# assert test_velocity(Point(17, -4), t_ex) == (False, None)
# assert test_velocity(Point(6, 9), t_ex) == (True, 45)
# print(one(t_ex))
# print(one(t_in))

print("===two")
# print(two(t_ex))
print(two(t_in))
