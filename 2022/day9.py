#!/usr/bin/python3

from collections import namedtuple
from math import sqrt
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


Pos = namedtuple("Pos", "x y")


def distance(a, b):
    return int(sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2))


def move(p, d, n=1):
    x, y = p.x, p.y
    if d == "R":
        x += n
    elif d == "L":
        x -= n
    elif d == "U":
        y += n
    elif d == "D":
        y -= n
    return Pos(x, y)


def follow(tail, head):
    if distance(head, tail) == 1:
        return tail

    x, y = tail.x, tail.y
    if tail.x != head.x:
        x += 1 if head.x > tail.x else -1
    if tail.y != head.y:
        y += 1 if head.y > tail.y else -1
    return Pos(x, y)


def one(inp):
    head = Pos(0, 0)
    tail = Pos(0, 0)
    seen = set()
    for l in inp:
        d, n = l.split()
        for _ in range(int(n)):
            head = move(head, d)
            tail = follow(tail, head)
            seen.add(tail)
    print(len(seen))


def two(inp):
    knots = [Pos(0, 0) for _ in range(10)]
    seen = set()
    for l in inp:
        d, n = l.split()
        for _ in range(int(n)):
            knots[0] = move(knots[0], d)
            for i in range(1, 10):
                knots[i] = follow(knots[i], knots[i - 1])
            seen.add(knots[9])
    print(len(seen))


one(get_input())
two(get_input())
