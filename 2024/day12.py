from dataclasses import dataclass

from aoc import solution
from pytest import fixture


@dataclass(frozen=True)
class P:
    x: int
    y: int


@fixture
def example():
    return """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


NEIGHBORS = ((0, -1), (1, 0), (0, 1), (-1, 0))  # N, E, S, W
DIAGONALS = ((1, -1), (1, 1), (-1, 1), (-1, -1))  # NE, SE, SW, NW


@solution(1930, 1457298)
def one(puzzle_input):
    plants = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            plants[P(x, y)] = c

    cost = 0
    while plants:
        p, c = plants.popitem()
        region = {p}
        work = [p]
        perimeter = 0
        while work:
            p = work.pop()
            for dx, dy in NEIGHBORS:
                n = P(p.x + dx, p.y + dy)
                if plants.get(n, None) == c:
                    plants.pop(n)
                    region.add(n)
                    work.append(n)
                elif n not in region:
                    perimeter += 1
        cost += perimeter * len(region)
    return cost


@solution(1206, 921636)
def two(puzzle_input):
    plants = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            plants[P(x, y)] = c

    cost = 0
    while plants:
        p, c = plants.popitem()
        region = {p}
        work = [p]
        corners = 0
        while work:
            p = work.pop(0)
            different = [False] * 4
            for i, (dx, dy) in enumerate(NEIGHBORS):
                n = P(p.x + dx, p.y + dy)
                if plants.get(n, None) == c:
                    plants.pop(n)
                    region.add(n)
                    work.append(n)
                elif n not in region:
                    different[i] = True
            diagonals = [P(p.x + dx, p.y + dy) for (dx, dy) in DIAGONALS]
            for i in range(len(different)):
                if different[i] and different[(i + 1) % 4]:
                    corners += 1
                if (
                    not different[i]
                    and not different[(i + 1) % 4]
                    and diagonals[i] not in region
                    and plants.get(diagonals[i], None) != c
                ):
                    corners += 1

        cost += len(region) * corners
    return cost
