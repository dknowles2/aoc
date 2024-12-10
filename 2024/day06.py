from dataclasses import dataclass

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


@dataclass(frozen=True)
class P:
    x: int
    y: int


@solution(41, 5199)
def one(puzzle_input):
    h, w, d, p = 0, 0, "up", P(0, 0)
    obstacles, seen = set(), set()
    for y, line in enumerate(puzzle_input.splitlines()):
        h += 1
        w = len(line)
        for x, c in enumerate(line):
            if c == "#":
                obstacles.add(P(x, y))
            elif c == "^":
                p = P(x, y)
                seen.add(p)

    while p.x >= 0 and p.x < w and p.y >= 0 and p.y < h:
        seen.add(p)
        next = {
            "up": P(p.x, p.y - 1),
            "down": P(p.x, p.y + 1),
            "left": P(p.x - 1, p.y),
            "right": P(p.x + 1, p.y),
        }[d]
        if next in obstacles:
            d = {
                "up": "right",
                "down": "left",
                "left": "up",
                "right": "down",
            }[d]
        else:
            p = next
    return len(seen)


@solution(6, 1915)
def two(puzzle_input):
    h, w, start = 0, 0, P(0, 0)
    obstacles = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        h += 1
        w = len(line)
        for x, c in enumerate(line):
            if c == "#":
                obstacles.add(P(x, y))
            elif c == "^":
                start = P(x, y)

    def check(obstacles, o):
        p, d, seen = start, "up", set()
        while p.x >= 0 and p.x < w and p.y >= 0 and p.y < h:
            if o and (p, d) in seen:
                return True, seen
            seen.add((p, d))
            next = {
                "up": P(p.x, p.y - 1),
                "down": P(p.x, p.y + 1),
                "left": P(p.x - 1, p.y),
                "right": P(p.x + 1, p.y),
            }[d]
            if next in obstacles | {o}:
                d = {
                    "up": "right",
                    "down": "left",
                    "left": "up",
                    "right": "down",
                }[d]
            else:
                p = next
        return False, seen

    _, seen = check(obstacles, None)
    ret = 0
    for p in {p for p, _ in seen}:
        if p == start:
            continue
        has_cycle, _ = check(obstacles, p)
        if has_cycle:
            ret += 1
    return ret
