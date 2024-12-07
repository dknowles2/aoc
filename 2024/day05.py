from functools import cache

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


@solution(143, 4996)
def one(puzzle_input):
    rules = []

    def check(update):
        for a, b in rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    return False
        return True

    ret = 0
    for line in puzzle_input.splitlines():
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            update = line.split(",")
            if check(update):
                ret += int(update[len(update) // 2])
    return ret


@solution(123, 6311)
def two(puzzle_input):
    rules = []

    def check(update):
        lt, ok = {}, True
        for a, b in rules:
            if a in update and b in update:
                lt.setdefault(a, []).append(b)
                if update.index(a) > update.index(b):
                    ok = False

        if ok:
            return update

        @cache
        def fix(a):
            for b in lt.get(a, []):
                fix(b)
                ai, bi = update.index(a), update.index(b)
                if ai > bi:
                    update.insert(bi, update.pop(ai))

        for n in update[:]:
            fix(n)

        return update

    ret = 0
    for line in puzzle_input.splitlines():
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            update = line.split(",")
            ordered = check(update[:])
            if update != ordered:
                ret += int(ordered[len(ordered) // 2])
    return ret
