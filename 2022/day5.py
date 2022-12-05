#!/usr/bin/python3


def read_input():
    from pathlib import Path

    me = Path(__file__)
    return Path(me.parent / "input" / (me.stem + ".txt")).read_text().splitlines()


def parse():
    stacks = [[] for _ in range(9)]
    moves = []
    for l in read_input():
        if l.startswith("move"):
            _, n, _, f, _, t = l.split()
            moves.append((int(n), int(f) - 1, int(t) - 1))
        elif "[" in l:
            for i in range(9):
                if c := l[(i * 4) + 1].strip():
                    stacks[i].insert(0, c)
    return stacks, moves


def one():
    stacks, moves = parse()
    for n, f, t in moves:
        for _ in range(n):
            stacks[t].append(stacks[f].pop())
    print("".join(s.pop() for s in stacks))


def two():
    stacks, moves = parse()
    for n, f, t in moves:
        stacks[t].extend(stacks[f][-n:])
        stacks[f] = stacks[f][:-n]
    print("".join(s.pop() for s in stacks))


one()
two()
