import re
from dataclasses import dataclass, field
from math import prod

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


@solution(4277556, 4076006202939, run_puzzle=True)
def one(puzzle_input):
    lines = puzzle_input.splitlines()
    problems = [[] for _ in lines[0].split()]
    for line in lines[:-1]:
        for i, n in enumerate(line.split()):
            problems[i].append(int(n))

    ops = {
        "*": prod,
        "+": sum,
    }
    ret = 0
    for i, op in enumerate(lines[-1].split()):
        ret += ops[op](problems[i])

    return ret


@dataclass
class Problem:
    op: str
    col: tuple[int, int]
    items: list = field(default_factory=list)

    def run(self) -> int:
        args = []
        for i in reversed(range(0, self.col[1] - self.col[0])):
            if n := "".join(c[i] for c in reversed(self.items)).strip():
                args.append(int(n))
        return {"*": prod, "+": sum}[self.op](args)


@solution(3263827, 7903168391557, run_puzzle=True)
def two(puzzle_input):
    problems: list[Problem] = []
    for i, line in enumerate(reversed(puzzle_input.splitlines())):
        if i == 0:
            problems = [
                Problem(m.group(2), m.span(1), [])
                for m in re.finditer(r"(([\*\+]) *)", line)
            ]
        else:
            for p in problems:
                p.items.append(line[p.col[0] : p.col[1]])
    return sum(p.run() for p in problems)
