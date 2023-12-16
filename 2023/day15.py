from dataclasses import dataclass, field
from pathlib import Path
import re

from util import check, get_input


example = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".splitlines


def one(input_fn=get_input):
    ret = 0
    for s in input_fn()[0].split(","):
        ret += do_hash(s)
    return ret


@dataclass
class Box:
    values: dict[str, int] = field(default_factory=dict)  # {label: value}
    lenses: list[str] = field(default_factory=list)  # [label]

    def add(self, label, value):
        if label not in self.values:
            self.lenses.append(label)
        self.values[label] = value

    def remove(self, label):
        if (i := self.values.pop(label, None)) is not None:
            self.lenses.remove(label)


def two(input_fn=get_input):
    boxes = [Box() for _ in range(256)]
    for s in input_fn()[0].split(","):
        label, op, num = re.match(r"([a-z]+)([-=])([0-9]+)?", s).groups()
        h = do_hash(label)
        if op == "-":
            boxes[h].remove(label)
        else:
            boxes[h].add(label, int(num))

    ret = 0
    for i, b in enumerate(boxes):
        for j, l in enumerate(b.lenses):
            ret += (1 + i) * (1 + j) * b.values[l]
    return ret


def do_hash(s, i=0):
    for c in s:
        i = (17 * (i + ord(c))) % 256
    return i


check(do_hash("HASH"), 52)
check(one(example), 1320)
print(one())
check(two(example), 145)
print(two())
