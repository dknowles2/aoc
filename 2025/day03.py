from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def joltage(batteries: list[int], enable: int) -> int:
    mi, m = -1, None
    for i, n in enumerate(batteries[0 : len(batteries) - (enable - 1)]):
        if m is None or n > m:
            mi, m = i, n

    final = [m]
    while len(final) < enable:
        m = None
        slice = batteries[mi + 1 : len(batteries) - (enable - 1 - len(final))]
        for i, n in enumerate(slice, start=mi + 1):
            if m is None or n > m:
                mi, m = i, n
        final.append(m)

    return int("".join(map(str, final)))


@solution(357, 17324)
def one(puzzle_input):
    return sum(joltage([int(c) for c in line], 2) for line in puzzle_input.splitlines())


@solution(3121910778619, 171846613143331, run_puzzle=True)
def two(puzzle_input):
    return sum(
        joltage([int(c) for c in line], 12) for line in puzzle_input.splitlines()
    )
