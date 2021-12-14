#!/usr/bin/python3

from collections import defaultdict as ddict
from collections import deque
from copy import deepcopy

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read()

ex1 = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

ex2 = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

ex3 = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def parse(xin):
    segs = ddict(list)
    for seg in xin.strip().split("\n"):
        a, b = seg.split("-")
        if b == 'start' or a == 'end':
            a, b = b, a
        segs[a].append(b)
        if a != 'start' and b != 'end':
            segs[b].append(a)
    return segs


def num_paths(xin):
    segs = parse(xin)
    paths = []
    q = deque((['start'], n) for n in segs['start'])
    while q:
        cur, n = q.popleft()
        if n.islower() and n in cur:
            continue
        if n == 'end':
            paths.append(cur + [n])
        else:
            q.extendleft((cur + [n], x) for x in segs[n])

    print(len(paths))


class Path:
    def __init__(self):
        self.has_lower = False
        self._p = ['start']

    def __contains__(self, n):
        return n in self._p

    def __len__(self):
        return len(self._p)

    def __str__(self):
        return ",".join(self._p)

    def append(self, n):
        if n.islower() and n in self._p:
            self.has_lower = True
        self._p.append(n)


def num_paths2(xin):
    segs = parse(xin)
    paths = set()
    q = deque((Path(), n) for n in segs['start'])
    while q:
        cur, n = q.popleft()
        if n == 'end':
            cur = deepcopy(cur)
            cur.append(n)
            paths.add(cur)
        elif n.islower() and cur.has_lower and n in cur:
            continue
        else:
            for x in segs[n]:
                c = deepcopy(cur)
                c.append(n)
                q.appendleft((c, x))

    print(len(paths))


num_paths(ex1)
num_paths(ex2)
num_paths(ex3)
num_paths(in1)

print('===two')
num_paths2(ex1)
num_paths2(ex2)
num_paths2(ex3)
num_paths2(in1)
