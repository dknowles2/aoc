#!/usr/bin/python3

from collections import namedtuple

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read()

ex1 = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

Coord = namedtuple("Coord", "x y")
Fold = namedtuple("Fold", "axis line")


class Paper:

    def __init__(self, dots, w, h):
        self.dots = dots
        self.w = w
        self.h = h

    def __str__(self):
        s = ""
        for y in range(self.h+1):
            for x in range(self.w+1):
                s += "#" if (x, y) in self.dots else "."
            s += "\n"
        return s

    def fold(self, fold):
        new_dots = set()
        w = 0 if fold.axis == "y" else fold.line
        h = 0 if fold.axis == "x" else fold.line
        for dot in self.dots:
            dotd = {"x": dot.x, "y": dot.y}
            for a, v in dotd.items():
                if a != fold.axis or dotd[a] <= fold.line:
                    continue
                dotd[a] = fold.line + fold.line - dotd[a]
            if dotd["x"] >=0 and dotd["y"] >= 0:
                w = max(w, dotd["x"])
                h = max(h, dotd["y"])
                new_dots.add(Coord(**dotd))
        self.dots = new_dots
        self.w = w
        self.h = h


def parse(xin):
    dots = set()
    folds = []
    w, h = 0, 0
    for l in xin.split("\n"):
        if not l:
            continue
        elif l.startswith("fold along "):
            axis, v = l.replace("fold along ", "").split("=")
            folds.append(Fold(axis, int(v)))
        else:
            x, y = map(int, l.split(","))
            dots.add(Coord(x, y ))
            w = max(w, x)
            h = max(h, y)

    return Paper(dots, w, h), folds


def one(xin):
    paper, folds = parse(xin)
    paper.fold(folds[0])
    print(len(paper.dots))

def two(xin):
    paper, folds = parse(xin)
    for f in folds:
        paper.fold(f)
    print(paper)


one(ex1)
one(in1)
print()
print("===two")
two(ex1)
two(in1)
