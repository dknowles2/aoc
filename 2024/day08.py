from dataclasses import dataclass
from itertools import combinations
from string import ascii_letters, digits

from aoc import solution
from pytest import fixture


@dataclass(frozen=True)
class P:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"


@fixture
def example():
    return """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


@solution(14, 285)
def one(puzzle_input):
    grid: set[P] = set()
    antennas: dict[str, list[P]] = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            p = P(x, y)
            grid.add(p)
            if c in ascii_letters + digits:
                antennas.setdefault(c, []).append(p)

    antinodes: set[P] = set()
    for pts in antennas.values():
        for a, b in combinations(pts, 2):
            xd = abs(a.x - b.x)
            yd = abs(a.y - b.y)
            top = P(a.x - xd if a.x < b.x else a.x + xd, a.y - yd)
            if top in grid:
                antinodes.add(top)
            btm = P(b.x - xd if b.x < a.x else b.x + xd, b.y + yd)
            if btm in grid:
                antinodes.add(btm)
    return len(antinodes)


@solution(34, 944)
def two(puzzle_input):
    grid: set[P] = set()
    antennas: dict[str, list[P]] = {}
    all_antennas: set[P] = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            p = P(x, y)
            grid.add(p)
            if c in ascii_letters + digits:
                antennas.setdefault(c, []).append(p)
                all_antennas.add(p)

    def get_antinodes(a, b, up=True, dn=True):
        xd = abs(a.x - b.x)
        yd = abs(a.y - b.y)
        if up:
            tx = a.x - xd if a.x < b.x else a.x + xd
            top = P(tx, a.y - yd)
            if top in grid:
                antinodes.add(top)
                get_antinodes(top, a, dn=False)

        if dn:
            bx = b.x - xd if b.x < a.x else b.x + xd
            btm = P(bx, b.y + yd)
            if btm in grid:
                antinodes.add(btm)
                get_antinodes(b, btm, up=False)

    antinodes: set[P] = set()
    for pts in antennas.values():
        for a, b in combinations(pts, 2):
            get_antinodes(a, b)

    return len(antinodes | all_antennas)
