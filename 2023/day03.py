from dataclasses import dataclass

from util import get_input


example = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def is_symbol(c: str) -> bool:
    return c not in "1234567890."


def is_number(c: str) -> bool:
    return c in "1234567890"


def one():
    input_ = example.splitlines()
    input_ = get_input()
    symbols = {}  # (x, y) -> str
    numbers = {}  # (y, x0, x1) -> int
    max_x, max_y = len(input_) - 1, len(input_[0]) - 1
    for y, line in enumerate(input_):
        n, x0 = "", None
        for x, c in enumerate(line):
            if is_number(c):
                n += c
                x0 = x if x0 is None else x0
            else:
                if n:
                    numbers[(y, x0, x)] = int(n)
                    n, x0 = "", None
                if is_symbol(c):
                    symbols[(x, y)] = c
        if n:
            numbers[(y, x0, x)] = int(n)

    def has_adj(y, x0, x1):
        if x0 > 0:
            if sym := symbols.get((x0 - 1, y)):
                return sym
        if x1 < max_x:
            if sym := symbols.get((x1, y)):
                return sym
        if y > 0:
            for x in range(max(0, x0 - 1), min(max_x, x1 + 1)):
                if sym := symbols.get((x, y - 1)):
                    return sym
        if y < max_y:
            for x in range(max(0, x0 - 1), min(max_x, x1 + 1)):
                if sym := symbols.get((x, y + 1)):
                    return sym
        return None

    ret = 0
    for (y, x0, x1), num in numbers.items():
        sym = has_adj(y, x0, x1)
        if sym:
            ret += num
    print(ret)


@dataclass(frozen=True, eq=False)
class Number:
    value: int


def two():
    input_ = example.splitlines()
    input_ = get_input()

    gears: set[tuple[int, int]] = set()  # {(x, y), ...}
    numbers: dict[tuple[int, int], Number] = {}  # (x, y) -> int
    max_x, max_y = len(input_), len(input_[0])

    def add_number(x0: int, x1: int, y: int, n: int):
        nn = Number(n)
        for x in range(x0, x1 + 1):
            numbers[(x, y)] = nn

    for y, line in enumerate(input_):
        n, x0 = "", None
        for x, c in enumerate(line):
            if is_number(c):
                n += c
                if x0 is None:
                    x0 = x
            else:
                if n:
                    add_number(x0, x - 1, y, int(n))
                    n, x0 = "", None
                if c == "*":
                    gears.add((x, y))
        if n:
            add_number(x0, x, y, int(n))

    def get_adj(x: int, y: int) -> set[int]:
        adj: set[int] = set()
        if x > 0 and (n := numbers.get((x - 1, y))):
            adj.add(n)
        if x < max_x and (n := numbers.get((x + 1, y))):
            adj.add(n)

        if y > 0:
            for xx in range(max(0, x - 1), min(max_x, x + 2)):
                if n := numbers.get((xx, y - 1)):
                    adj.add(n)
        if y < max_y:
            for xx in range(max(0, x - 1), min(max_x, x + 2)):
                if n := numbers.get((xx, y + 1)):
                    adj.add(n)
        return adj

    ret = 0
    for x, y in sorted(gears, key=lambda x: (x[1], x[0])):
        adj = get_adj(x, y)
        if len(adj) == 2:
            a, b = adj
            ret += a.value * b.value
    print(ret)


one()
two()
