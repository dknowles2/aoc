from collections import namedtuple
from itertools import combinations
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


example = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".splitlines


class Pos(namedtuple("Pos", "x y")):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def expand(self, x_exp, y_exp, m):
        return Pos(
            self.x + (x_exp[self.x] * m) - x_exp[self.x],
            self.y + (y_exp[self.y] * m) - y_exp[self.y],
        )


def dist(input_fn=get_input, expansion=2):
    image = input_fn()
    galaxies = []
    h = len(image)
    w = len(image[0])
    rows = [False] * h
    cols = [False] * w
    for y, line in enumerate(image):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append(Pos(x, y))
                rows[y] = True
                cols[x] = True

    y_exp = [0] * h
    for i, b in enumerate(rows):
        if b:
            continue
        for n in range(i, h):
            y_exp[n] += 1
    x_exp = [0] * w
    for i, b in enumerate(cols):
        if b:
            continue
        for n in range(i, w):
            x_exp[n] += 1

    ret = 0
    for a, b in combinations(galaxies, 2):
        a = a.expand(x_exp, y_exp, expansion)
        b = b.expand(x_exp, y_exp, expansion)
        x_dist = abs(a.x - b.x)
        y_dist = abs(a.y - b.y)
        ret += x_dist + y_dist
    return ret


def check(a, b):
    assert a == b, f"{a} != {b}"


check(dist(example), 374)
print(dist())
check(dist(example, expansion=10), 1030)
check(dist(example, expansion=100), 8410)
print(dist(expansion=1_000_000))
