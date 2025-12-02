from functools import cache

from aoc import solution
from pytest import fixture


@fixture
def example():
    return "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


@solution(1227775554, 53420042388)
def one(puzzle_input):
    invalid = []
    for num_range in puzzle_input.strip().split(","):
        start, end = map(int, num_range.split("-"))
        for num in range(start, end + 1):
            snum = str(num)
            if len(snum) % 2 != 0:
                continue
            if snum == snum[0 : len(snum) // 2] * 2:
                invalid.append(num)
    return sum(invalid)


@solution(4174379265, 69553832684)
def two(puzzle_input):
    @cache
    def check(num: str) -> bool:
        for i in range(1, len(num) // 2 + 1):
            sub = num[0:i]
            if num == sub * (len(num) // len(sub)):
                return True
        return False

    invalid = []
    for num_range in puzzle_input.strip().split(","):
        start, end = map(int, num_range.split("-"))
        for num in range(start, end + 1):
            if check(str(num)):
                invalid.append(num)
    return sum(invalid)
