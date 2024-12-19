import sys
from dataclasses import dataclass
from functools import reduce
from itertools import product
from operator import mul
from os import environ

if "PYTEST_CURRENT_TEST" not in environ:
    sys.path.insert(0, "..")

from aoc import get_input, solution
from pytest import fixture

_EXAMPLE = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


@fixture
def example():
    return _EXAMPLE


@dataclass(frozen=True)
class P:
    x: int
    y: int


@dataclass
class Robot:
    p: P
    v: P


@solution(12, 222062148)
def one(puzzle_input):
    is_example = puzzle_input == _EXAMPLE
    w = 11 if is_example else 101
    h = 7 if is_example else 103
    return run(puzzle_input, w, h)


def run(puzzle_input, w, h, count=100, step=False):
    robots: list[Robot] = []
    for line in puzzle_input.splitlines():
        p_str, v_str = line.split(" ")
        p = P(*map(int, p_str[2:].split(",")))
        v = P(*map(int, v_str[2:].split(",")))
        robots.append(Robot(p, v))

    def add_p(p: P, v: P):
        return P((p.x + v.x) % w, (p.y + v.y) % h)

    mw, mh = w // 2, h // 2
    tiles: dict[P, int] = {}
    quadrants = [0, 0, 0, 0]
    for i in range(count):
        for r in robots:
            r.p = add_p(r.p, r.v)
            if step:
                tiles[r.p] = True
            if not step and i == 99:
                if r.p.x == mw or r.p.y == mh:
                    continue
                q_x = 0 if r.p.x < w // 2 else 1
                q_y = 0 if r.p.y < h // 2 else 1
                quadrants[(2 * q_x) + q_y] += 1

        if step:
            if not any(
                True
                and P(x, y) in tiles
                and P(x - 1, y - 1) in tiles
                and P(x - 1, y + 1) in tiles
                and P(x + 1, y + 1) in tiles
                and P(x + 1, y - 1) in tiles
                and P(x - 1, y) in tiles
                and P(x + 1, y) in tiles
                and P(x, y - 1) in tiles
                and P(x, y + 1) in tiles
                for x, y in product(range(1, w - 1), range(1, h - 1))
            ):
                tiles = {}
                continue
            for y in range(0, h):
                for x in range(0, w):
                    print("x" if tiles.get(P(x, y), False) else " ", end="")
                print()
            input(f"{i+1} > ")
            tiles = {}

    return reduce(mul, quadrants)


if __name__ == "__main__":
    run(get_input(), 101, 103, 100000, True)
