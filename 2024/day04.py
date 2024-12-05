from itertools import product

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


@solution(18, 2406)
def one(puzzle_input):
    grid = puzzle_input.splitlines()
    w, h = len(grid[0]), len(grid)

    def dh(ix, iy):
        sx, tx = ix, ix + 4
        return "".join(grid[iy][sx:tx])

    def dv(ix, iy):
        ty = min(h, iy + 4)
        return "".join(grid[y][ix] for y in range(iy, ty))

    def dr(ix, iy):
        tx, ty = min(w, ix + 4), min(h, iy + 4)
        return "".join(grid[y][x] for x, y in zip(range(ix, tx), range(iy, ty)))

    def dl(ix, iy):
        tx, ty = max(-1, ix - 4), min(h, iy + 4)
        return "".join(grid[y][x] for x, y in zip(range(ix, tx, -1), range(iy, ty)))

    return sum(
        f(x, y) in ("XMAS", "SAMX")
        for f in (dh, dv, dr, dl)
        for x, y in product(range(w), range(h))
    )


@solution(9, 1807)
def two(puzzle_input):
    grid = puzzle_input.splitlines()
    w, h = len(grid[0]), len(grid)

    def mas(x, y):
        a = grid[y - 1][x - 1] + grid[y + 1][x + 1]
        b = grid[y - 1][x + 1] + grid[y + 1][x - 1]
        c = grid[y][x]
        return a in ("MS", "SM") and b in ("MS", "SM") and c == "A"

    return sum(mas(x, y) for x, y in product(range(1, w - 1), range(1, h - 1)))
