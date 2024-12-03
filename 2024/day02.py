from functools import cache

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()


def pop(it, i):
    return it[:i] + it[i + 1 :]


@cache
def check(it, can_remove=False):
    is_inc, prev = None, None
    for i, n in enumerate(it):
        if prev is not None:
            n_gt = n > prev
            if is_inc is None:
                is_inc = n_gt
            elif is_inc != n_gt:
                return can_remove and any(check(pop(it, j)) for j in [i - 2, i - 1, i])
            if not (0 < abs(n - prev) < 4):
                return can_remove and any(check(pop(it, j)) for j in [i - 1, i])
        prev = n
    return True


@solution(2, 442)
def one(puzzle_input):
    return sum(check(tuple(int(n) for n in l.split())) for l in puzzle_input)


@solution(4, 493)
def two(puzzle_input):
    return sum(check(tuple(int(n) for n in l.split()), True) for l in puzzle_input)
