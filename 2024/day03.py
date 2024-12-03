import re

from aoc import solution
from pytest import fixture


@fixture
def example1():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


@fixture
def example2():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


_MUL_RE = re.compile(r"(?s)mul\(([0-9]{1,3}),([0-9]{1,3})\)$")
_DO_RE = re.compile(r"(?s)do\(\)$")
_DONT_RE = re.compile(r"(?s)don't\(\)$")
_RESET_RE = re.compile(r"(?s).*(mul|do|don't)$")


@solution(161, 178794710)
def one(puzzle_input):
    ret = 0
    word = ""
    for c in puzzle_input:
        word += c
        if len(word) >= 3 and word[-3:] == "mul":
            word = "mul"
            continue
        if len(word) < 8:
            continue
        if match := _MUL_RE.match(word):
            a, b = match.groups()
            ret += int(a) * int(b)
            word = ""
    return ret


@solution(48, 76729637)
def two(puzzle_input):
    enabled = True
    ret = 0
    word = ""
    for c in puzzle_input:
        word += c
        if m := _RESET_RE.match(word):
            word = word[-len(m.groups()[0]) :]
            continue
        if _DONT_RE.match(word):
            enabled = False
            word = ""
        elif _DO_RE.match(word):
            enabled = True
            word = ""
        elif enabled and (m := _MUL_RE.match(word)):
            a, b = m.groups()
            ret += int(a) * int(b)
            word = ""
    return ret
