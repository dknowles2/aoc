#!/usr/bin/python3

from collections import Counter
from pathlib import Path


def find_marker(buf, n):
    for i in range(n, len(buf) + 1):
        if len(Counter(buf[i - n : i])) == n:
            return i
    return -1


def one(buf):
    print(find_marker(buf, 4))


def two(buf):
    print(find_marker(buf, 14))


me = Path(__file__)
[buf] = Path(me.parent / "input" / (me.stem + ".txt")).read_text().splitlines()
one(buf)
two(buf)
