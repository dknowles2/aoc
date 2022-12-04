#!/usr/bin/python3

from collections import defaultdict

elves = defaultdict(int)

with open("input/day1.txt") as data:
    e = 0
    for l in data.readlines():
        l = l.strip()
        if l == "":
            e += 1
            continue
        elves[e] += int(l)

print(max(elves.values()))
print(sum(sorted(elves.values(), reverse=True)[0:3]))
