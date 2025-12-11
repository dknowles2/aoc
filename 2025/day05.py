from dataclasses import dataclass, field

from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


@solution(3, 888)
def one(puzzle_input):
    ranges = []
    fresh = 0
    for line in puzzle_input.splitlines():
        if "-" in line:
            lower, upper = map(int, line.split("-"))
            ranges.append((lower, upper))
        elif line:
            id = int(line)
            for lower, upper in ranges:
                if lower <= id <= upper:
                    fresh += 1
                    break

    return fresh


@dataclass(repr=False)
class Range:
    lower: int
    upper: int
    next: "Range | None" = field(default=None, repr=False)

    def __repr__(self) -> str:
        return f"{self.lower}-{self.upper}"

    @property
    def count(self) -> int:
        return 1 + self.upper - self.lower

    def merge_right(self):
        while self.next and mergeable(self, self.next):
            self.lower = min(self.lower, self.next.lower)
            self.upper = max(self.upper, self.next.upper)
            self.next = self.next.next


def mergeable(a: Range, b: Range) -> bool:
    if a.lower <= b.lower:
        first, second = a, b
    else:
        first, second = b, a

    if first.upper == second.lower:
        return True
    return (first.upper + 1) >= second.lower


@solution(14, 344378119285354, run_puzzle=True)
def two(puzzle_input):
    first = None
    for line in puzzle_input.splitlines():
        if "-" not in line:
            break
        lower, upper = map(int, line.split("-"))
        this = Range(lower, upper)
        if first is None:
            first = this
            continue

        prev, r = None, first
        merged = False
        while r and not merged:
            if mergeable(r, this):
                this.next = r
                this.merge_right()
                if prev:
                    prev.next = this
                merged = True
                if r == first:
                    first = this
            else:
                prev = r
                r = r.next
        if merged:
            continue

        prev = None
        this.next = first
        moved = False
        while this.next and this.lower > this.next.upper:
            prev = this.next
            this.next = this.next.next
            moved = True
        if not moved:
            first = this
        if prev:
            prev.next = this

    fresh = 0
    r = first
    while r:
        fresh += r.count
        r = r.next

    return fresh
