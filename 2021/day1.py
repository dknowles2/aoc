#!/usr/bin/python3

"""Initially written on an iPad in Antigua :-)"""

with open("input/" + __file__.replace(".py", ".txt")) as f:
    input1 = f.readlines()

ex = """\
199
200
208
210
200
207
240
269
260
263
""".strip().split("\n")

def one(m):
    inc = 0
    last = None
    for d in map(int, m):
        if last is not None and d > last:
            inc += 1
        last = d

    print(inc)

one(ex)
one(input1)

print("### two")

def two(m):
    inc = 0
    for i, d in enumerate(map(int, m)):
        if i < 3:
            continue
        c = m[i] + m[i-1]+ m[i-2]
        p = m[i-1] + m[i-2] + m[i-3]
        if c > p:
            inc += 1
    print(inc)

two(ex)
two(input1)
