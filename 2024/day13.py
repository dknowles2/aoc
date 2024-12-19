from dataclasses import dataclass
from re import compile
from sys import maxsize as maxint

from aoc import solution
from pytest import fixture, skip


@fixture
def example():
    return """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


_LINE_RE = compile(r".+: X.([0-9]+), Y.([0-9]+)")


@dataclass(frozen=True)
class P:
    x: int = 0
    y: int = 0

    def __mul__(self, n: int) -> "P":
        return P(self.x * n, self.y * n)

    def __add__(self, other: "P") -> "P":
        return P(self.x + other.x, self.y + other.y)


@dataclass
class Machine:
    button_a: P = P()
    button_b: P = P()
    prize: P = P()


@solution(480, 25629)
def _one(puzzle_input):
    machines: list[Machine] = []
    for i, line in enumerate(puzzle_input.splitlines()):
        if ":" not in line:
            continue
        try:
            x, y = _LINE_RE.match(line).groups()
        except AttributeError:
            raise ValueError(f"'{line}' does not match regexp")
        p = P(int(x), int(y))
        if line.startswith("Button A:"):
            machines.append(Machine())
            machines[-1].button_a = p
        elif line.startswith("Button B:"):
            machines[-1].button_b = p
        elif line.startswith("Prize:"):
            machines[-1].prize = p

    total_cost = 0
    for m in machines:
        min_cost = maxint
        for da in range(0, 100):
            for db in range(0, 100):
                if (m.button_a * da) + (m.button_b * db) == m.prize:
                    cost = (3 * da) + db
                    if cost < min_cost:
                        min_cost = cost
        if min_cost != maxint:
            total_cost += min_cost
    return total_cost
