from bisect import insort
from dataclasses import dataclass
from random import randint
from sys import maxsize
from util import check, get_input

example = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".splitlines


@dataclass
class Rock:
    t: str
    x: int
    y: int


class DishView:
    def __init__(self, data):
        self.hash = 0
        self.zobrist = {}
        self.seen = {}
        self.w = len(data[0])
        self.h = len(data)
        self.x = [[] for _ in range(self.w)]
        self.y = [[] for _ in range(self.h)]
        self.rocks = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                v = randint(0, maxsize)
                self.zobrist[(x, y)] = v
                if c == ".":
                    continue
                if c == "O":
                    self.hash ^= v
                r = Rock(c, x, y)
                self.x[x].append(r)
                self.y[y].append(r)
                self.rocks[(x, y)] = r
        self.seen[self.hash] = 0

    def print(self):
        for y in range(self.h):
            for x in range(self.w):
                if r := self.rocks.get((x, y), None):
                    print(r.t, end="")
                else:
                    print(".", end="")
            print()

    def shift_rock(self, r, x, y):
        self.hash ^= self.zobrist[(r.x, r.y)]
        self.rocks.pop((r.x, r.y), None)
        if r.x != x:
            self.x[r.x].remove(r)
            r.x = x
            insort(self.x[r.x], r, key=lambda r: r.y)
        elif r.y != y:
            self.y[r.y].remove(r)
            r.y = y
            insort(self.y[r.y], r, key=lambda r: r.x)
        self.rocks[(r.x, r.y)] = r
        self.hash ^= self.zobrist[(r.x, r.y)]

    def cycle(self):
        self.shift_up()
        self.shift_left()
        self.shift_down()
        self.shift_right()

    def shift_up(self):
        for x in range(self.w):
            for i, r in enumerate(self.x[x]):
                if r.t == "#":
                    continue
                prev = self.x[x][i - 1] if i > 0 else Rock("O", x, -1)
                self.shift_rock(r, r.x, prev.y + 1)

    def shift_down(self):
        for x in range(self.w):
            lx = len(self.x[x]) - 1
            for i in range(lx, -1, -1):
                r = self.x[x][i]
                if r.t == "#":
                    continue
                next = self.x[x][i + 1] if i < lx else Rock("O", x, self.h)
                self.shift_rock(r, r.x, next.y - 1)

    def shift_left(self):
        for y in range(self.h):
            for i, r in enumerate(self.y[y]):
                if r.t == "#":
                    continue
                prev = self.y[y][i - 1] if i > 0 else Rock("O", -1, y)
                self.shift_rock(r, prev.x + 1, r.y)

    def shift_right(self):
        for y in range(self.h):
            ly = len(self.y[y]) - 1
            for i in range(ly, -1, -1):
                r = self.y[y][i]
                if r.t == "#":
                    continue
                next = self.y[y][i + 1] if i < ly else Rock("O", self.w, y)
                self.shift_rock(r, next.x - 1, r.y)


def one(input_fn=get_input):
    dv = DishView(input_fn())
    dv.shift_up()
    ret = 0
    for y in range(dv.h):
        ret += (dv.h - y) * sum(1 for r in dv.y[y] if r.t == "O")
    return ret


def two(input_fn=get_input):
    dv = DishView(input_fn())
    i = 0
    cycles = 1_000_000_000
    while i < cycles:
        dv.cycle()
        if ih := dv.seen.get(dv.hash, None):
            j = i - ih
            while i + j < cycles:
                i += j
        else:
            dv.seen[dv.hash] = i
        i += 1

    ret = 0
    for y in range(dv.h):
        ret += (dv.h - y) * sum(1 for r in dv.y[y] if r.t == "O")
    return ret


check(one(example), 136)
print(one())
check(two(example), 64)
print(two())
