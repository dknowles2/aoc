from collections import defaultdict as dd

elves = dd(int)

with open("input/day1.txt") as data:
    e = 0
    for l in data.readlines():
        l = l.strip()
        if l == "":
            e += 1
            continue
        elves[e] += int(l.strip())

print(max(elves.values()))

print(sum(sorted(elves.values() , reverse=True)[0:3]))
