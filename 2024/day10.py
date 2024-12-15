from dataclasses import dataclass

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


@dataclass(frozen=True)
class P:
    x: int
    y: int


@solution(36, 776)
def one(puzzle_input):
    trailheads = []
    trailmap: dict[P, int] = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, h in enumerate(list(map(int, line))):
            p = P(x, y)
            trailmap[p] = h
            if h == 0:
                trailheads.append(p)

    def walk(start: P):
        score = 0
        points = [start]
        seen = set()
        while points:
            p = points.pop()
            if p in seen:
                continue
            seen.add(p)
            if trailmap[p] == 9:
                score += 1
                continue
            for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                s = P(p.x + x, p.y + y)
                if s in trailmap and trailmap[s] - trailmap[p] == 1:
                    points.append(s)
        return score

    return sum(walk(p) for p in trailheads)


@solution(81, 1657)
def two(puzzle_input):
    trailheads = []
    trailmap: dict[P, int] = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, h in enumerate(list(map(int, line))):
            p = P(x, y)
            trailmap[p] = h
            if h == 0:
                trailheads.append(p)

    def walk(start: P):
        rating = 0
        points = [start]
        seen = set()
        while points:
            p = points.pop(0)
            seen.add(p)
            if trailmap[p] == 9:
                rating += 1
                continue
            for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                s = P(p.x + x, p.y + y)
                if s in seen:
                    continue
                if s in trailmap and trailmap[s] - trailmap[p] == 1:
                    points.append(s)
        return rating

    return sum(walk(p) for p in trailheads)
