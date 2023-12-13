from collections import namedtuple
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


DEBUG = False

example1 = """\
.....
.S-7.
.|.|.
.L-J.
.....""".splitlines

example2 = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".splitlines

example3 = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".splitlines


class Pos(namedtuple("Pos", "x y")):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"({self.x}, {self.y})"


conn_fns = {
    "|": lambda p: [Pos(p.x, p.y - 1), Pos(p.x, p.y + 1)],  # NS
    "-": lambda p: [Pos(p.x - 1, p.y), Pos(p.x + 1, p.y)],  # EW
    "L": lambda p: [Pos(p.x, p.y - 1), Pos(p.x + 1, p.y)],  # NE
    "J": lambda p: [Pos(p.x, p.y - 1), Pos(p.x - 1, p.y)],  # NW
    "7": lambda p: [Pos(p.x, p.y + 1), Pos(p.x - 1, p.y)],  # SW
    "F": lambda p: [Pos(p.x, p.y + 1), Pos(p.x + 1, p.y)],  # SE
    ".": lambda p: [],
}


def all_adj(p):
    return [
        Pos(p.x, p.y - 1),  # N
        Pos(p.x, p.y + 1),  # S
        Pos(p.x + 1, p.y),  # E
        Pos(p.x - 1, p.y),  # W
    ]


def find_start_pos(tiles):
    for y, line in enumerate(tiles):
        for x, c in enumerate(line):
            if c == "S":
                return Pos(x, y)


draw = {
    "S": "§",
    "-": "─",
    "7": "┐",
    "L": "└",
    "F": "┌",
    "J": "┘",
    "|": "│",
    ".": " ",
}


def print_tiles(tiles, seen=None, enclosed=None):
    for y, line in enumerate(tiles):
        for x, t in enumerate(line):
            p = Pos(x, y)
            if enclosed and p in enclosed:
                print("█", end="")
            elif seen and Pos(x, y) not in seen:
                print(" ", end="")
            else:
                print(draw[t], end="")
        print()


def find_path(tiles):
    w = len(tiles[0])
    h = len(tiles)
    is_valid = lambda p: p.x >= 0 and p.x < w and p.y >= 0 and p.y < h
    get_connections = lambda p: {c for c in conn_fns[tiles[p.y][p.x]](p) if is_valid(c)}
    start = find_start_pos(tiles)
    path = []
    for p in all_adj(start):
        if not is_valid(p):
            continue
        path = [start]
        prev = start
        conns = get_connections(p)
        while len(conns) == 2 and prev in conns:
            path.append(p)
            [next_p] = conns - {prev}
            prev = p
            p = next_p
            if p == start:
                return path
            conns = get_connections(p)


def one(input_fn=get_input):
    tiles = input_fn()
    path = find_path(tiles)
    if DEBUG:
        print_tiles(tiles, set(path))
    return len(path) // 2


def two(input_fn=get_input):
    tiles = input_fn()
    path = set(find_path(tiles))
    enclosed = set()
    for y, line in enumerate(tiles):
        intersects = 0
        for x, t in enumerate(line):
            if Pos(x, y) in path:
                if t in {"F", "7", "|"}:
                    intersects += 1
            elif intersects % 2 != 0:
                enclosed.add((x, y))
    if DEBUG:
        print_tiles(tiles, path, enclosed)
    return len(enclosed)


def check(a, b):
    assert a == b, f"{a} != {b}"


check(one(example1), 4)
check(one(example2), 8)
print(one())
check(two(example3), 10)
print(two())
