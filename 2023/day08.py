from itertools import cycle
from math import lcm
import re

from util import check, get_input


example1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".splitlines

example2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".splitlines


NODE_RE = re.compile(r"(?P<node>.{3}) = \((?P<L>.{3}), (?P<R>.{3})\)")


def one(input_fn=get_input):
    input_ = input_fn()
    dirs = cycle(input_[0])
    nodes = {}
    for line in input_[2:]:
        groups = NODE_RE.match(line).groupdict()
        nodes[groups.pop("node")] = groups

    node = "AAA"
    n = 0
    while node != "ZZZ":
        node = nodes[node][next(dirs)]
        n += 1
    return n


example3 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".splitlines


def two(input_fn=get_input):
    input_ = input_fn()
    dirs = input_[0]
    nodes = {}
    starts = []
    for line in input_[2:]:
        groups = NODE_RE.match(line).groupdict()
        node = groups.pop("node")
        nodes[node] = groups
        if node.endswith("A"):
            starts.append(node)

    ret = 1
    for node in starts:
        cdirs = cycle(dirs)
        n = 0
        while not node.endswith("Z"):
            node = nodes[node][next(cdirs)]
            n += 1
        ret = lcm(ret, n)

    return ret


check(one(example1), 2)
check(one(example2), 6)
print(one())
check(two(example3), 6)
print(two())
