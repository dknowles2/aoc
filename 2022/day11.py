#!/usr/bin/python3

from collections import deque
from dataclasses import dataclass
from math import lcm, prod
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


@dataclass
class Monkey:

    number: int
    items: deque
    inspect_l: str
    inspect_r: str
    inspect_op: str
    test_cond: int
    test_true: int
    test_false: int
    num_inspected: int

    def inspect(self, item):
        self.num_inspected += 1
        l = item if self.inspect_l == "old" else int(self.inspect_l)
        r = item if self.inspect_r == "old" else int(self.inspect_r)
        if self.inspect_op == "+":
            return l + r
        elif self.inspect_op == "*":
            return l * r


def parse(inp):
    monkeys = []
    current = None
    for l in inp:
        l = l.strip()
        if not l:
            continue

        k = l.split(":")[0]
        if k.startswith("Monkey"):
            current = Monkey(
                number=int(l.split(" ")[1].rstrip(":")),
                items=deque(),
                inspect_l="",
                inspect_r="",
                inspect_op="",
                test_cond=0,
                test_true=0,
                test_false=0,
                num_inspected=0,
            )
            monkeys.append(current)
            continue

        v = l.split(": ")[1]
        if k == "Starting items":
            current.items = deque([int(i.strip()) for i in v.split(", ")])
        elif k == "Operation":
            _, _, l, o, r = v.split(" ")
            current.inspect_l = l
            current.inspect_r = r
            current.inspect_op = o
        elif k == "Test":
            current.test_cond = int(v.split(" ")[-1])
        elif k == "If true":
            current.test_true = int(v.split(" ")[-1])
        elif k == "If false":
            current.test_false = int(v.split(" ")[-1])
    return monkeys


def one(inp):
    monkeys = parse(inp)

    for _ in range(20):
        for m in monkeys:
            while m.items:
                i = m.inspect(m.items.popleft()) // 3
                if i % m.test_cond == 0:
                    monkeys[m.test_true].items.append(i)
                else:
                    monkeys[m.test_false].items.append(i)

    print(prod(sorted([m.num_inspected for m in monkeys])[-2:]))


def two(inp):
    monkeys = parse(inp)
    m_lcm = lcm(*[m.test_cond for m in monkeys])

    for i in range(10000):
        for m in monkeys:
            while m.items:
                item = m.inspect(m.items.popleft()) % m_lcm
                if item % m.test_cond == 0:
                    monkeys[m.test_true].items.append(item)
                else:
                    monkeys[m.test_false].items.append(item)

    print(prod(sorted([m.num_inspected for m in monkeys])[-2:]))


one(get_input())
two(get_input())
