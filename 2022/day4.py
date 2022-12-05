#!/usr/bin/python3


def read_input():
    from pathlib import Path

    me = Path(__file__)
    return Path(me.parent / "input" / (me.stem + ".txt")).read_text().splitlines()


def parse_line(l):
    parse_range = lambda r: tuple(int(x) for x in r.split("-"))
    a, b = l.split(",")
    return parse_range(a), parse_range(b)


def one():
    ret = 0
    contains = lambda a, b: a[0] <= b[0] and a[1] >= b[1]
    for l in read_input():
        a, b = parse_line(l)
        if contains(a, b) or contains(b, a):
            ret += 1
    print(ret)


def two():
    ret = 0
    is_between = lambda x, r: r[0] <= x and r[1] >= x
    overlaps = lambda a, b: is_between(b[0], a) or is_between(b[1], a)
    for l in read_input():
        a, b = parse_line(l)
        if overlaps(a, b) or overlaps(b, a):
            ret += 1
    print(ret)


one()
two()
