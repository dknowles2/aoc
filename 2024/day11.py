from functools import cache
from math import floor, log

from aoc import solution
from pytest import fixture


@fixture
def example():
    return "125 17\n"


@cache
def count(value, i):
    if i == 0:
        return 1
    ret = 0
    if value == 0:
        ret += count(1, i - 1)
    elif (digits := floor(log(value, 10)) + 1) % 2 == 0:
        h = 10 ** (digits // 2)
        ret += count(value // h, i - 1)
        ret += count(value % h, i - 1)
    else:
        ret += count(value * 2024, i - 1)
    return ret


@solution(55312, 217812)
def one(puzzle_input):
    return sum(count(int(n), 25) for n in puzzle_input.strip().split())


@solution(65601038650482, 259112729857522)
def two(puzzle_input):
    return sum(count(int(n), 75) for n in puzzle_input.strip().split())
