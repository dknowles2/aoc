from aoc import get_input, solution
from pytest import fixture


@fixture
def example():
    return """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


@solution(3, 962)
def one(puzzle_input):
    s = 50
    z = 0
    for line in puzzle_input.splitlines():
        n = int(line[1:]) * (-1 if line[0] == "L" else 1)
        s = (s + n) % 100
        if s == 0:
            z += 1
    return z


@solution(6, 5782)
def two(puzzle_input):
    s = 50
    z = 0
    for line in puzzle_input.splitlines():
        d = int(line[1:])
        if line[0] == "R":
            z += (s + d) // 100
            s = (s + d) % 100
        else:
            if s > 0:
                z += ((d - s) // 100) + 1
            else:
                z += d // 100
            s = (s - d) % 100
    return z
