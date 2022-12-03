#!/usr/bin/python3

import string


def read_input():
    from os.path import basename
    with open("input/" + basename(__file__).replace(".py", ".txt")) as f:
        return f.readlines()


def priority(c):
    return string.ascii_letters.index(c) + 1


def one():
    res = 0
    for l in read_input():
        l = l.strip()
        m = int(len(l)/2)
        a, b = set(l[:m]), set(l[m:])
        res += priority(list(a&b)[0])
    print(res)


def two():
    res = 0
    s = set()
    for i, l in enumerate(read_input()):
        l = l.strip()
        if i % 3 == 0:
            s = set(l)
            continue
        s = s.intersection(set(l))
        if (i + 1) % 3 == 0:
            res += priority(list(s)[0])
    print(res)


one()
two()
