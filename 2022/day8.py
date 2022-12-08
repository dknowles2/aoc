#!/usr/bin/python3

from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


def get_trees():
    inp = get_input()
    h, w = len(inp), len(inp[0])
    trees = {}
    for y, l in enumerate(inp):
        for x, th in enumerate(list(l)):
            trees[(x, y)] = int(th)
    return trees, h, w


def one(trees, h, w):
    visible = set()
    for (x, y), th in trees.items():
        if x == 0 or y == 0 or x == w - 1 or y == h - 1:
            visible.add((x, y))
            continue
        l = max([trees[(n, y)] for n in range(0, x)])
        r = max([trees[(n, y)] for n in range(x + 1, w)])
        u = max([trees[(x, n)] for n in range(0, y)])
        d = max([trees[(x, n)] for n in range(y + 1, h)])
        if th > l or th > r or th > u or th > d:
            visible.add((x, y))
    print(len(visible))


def two(trees, h, w):
    scores = []
    for (x, y), th in trees.items():
        def num_shorter(it):
            ret = 0
            for t in it:
                if t <= th:
                    ret += 1
                if t == th:
                    return ret
            return ret
        l = num_shorter([trees[(n, y)] for n in range(x - 1, -1, -1)])
        r = num_shorter([trees[(n, y)] for n in range(x + 1, w)])
        u = num_shorter([trees[(x, n)] for n in range(y - 1, -1, -1)])
        d = num_shorter([trees[(x, n)] for n in range(y + 1, h)])
        scores.append(l * r * u * d)
    print(max(scores))


trees, h, w = get_trees()
one(trees, h, w)
two(trees, h, w)
