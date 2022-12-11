#!/usr/bin/python3

from collections import deque
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


def one(inp):
    x = 1
    c = 1
    inst = None
    prog = deque(inp)
    next_sample = 20
    sig_sum = 0
    while prog or inst:
        if c == next_sample:
            sig_sum += (c * x)
            next_sample += 40
        if inst:
            x += inst
            inst = None
        else:
            l = prog.popleft()
            if l.startswith("addx"):
                _, inst = l.split(" ")
                inst = int(inst)
        c += 1
    print(sig_sum)


def two(inp):
    x = 1
    c = 1
    inst = None
    prog = deque(inp)
    while prog or inst:
        hpos = (c - 1) % 40
        if hpos in (x - 1, x, x + 1):
            print("#", end="")
        else:
            print(".", end="")
        if hpos == 39:
            print()

        if inst:
            x += inst
            inst = None
        else:
            l = prog.popleft()
            if l.startswith("addx"):
                _, inst = l.split(" ")
                inst = int(inst)
        c += 1


one(get_input())
two(get_input())
