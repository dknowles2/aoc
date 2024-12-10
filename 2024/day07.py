from itertools import product

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def mul(x: tuple[int, int]) -> int:
    return x[0] * x[1]


@solution(3749, 850435817339)
def one(puzzle_input):
    ret = 0
    for line in puzzle_input.splitlines():
        tv, nums = line.split(": ")
        tv = int(tv)
        nums = [int(n) for n in nums.split()]
        for ops in set(product((sum, mul), repeat=len(nums) - 1)):
            v = nums[0]
            for op, n in zip(ops, nums[1:]):
                v = op((v, n))
            if v == tv:
                ret += v
                break
    return ret


def concat(x: tuple[int, int]) -> int:
    return int(str(x[0]) + str(x[1]))


@solution(11387, 104824810233437)
def two(puzzle_input):
    ret = 0
    for line in puzzle_input.splitlines():
        tv, nums = line.split(": ")
        tv = int(tv)
        nums = [int(n) for n in nums.split()]
        for ops in set(product((sum, mul, concat), repeat=len(nums) - 1)):
            v = nums[0]
            for op, n in zip(ops, nums[1:]):
                v = op((v, n))
            if v == tv:
                ret += v
                break
    return ret
