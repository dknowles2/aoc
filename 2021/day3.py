#!/usr/bin/python3

"""Initially written on an iPad in Antigua :-)"""

with open("input/" + __file__.replace(".py", ".txt")) as f:
    input1 = f.readlines()

ex = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip().split("\n")

def one(input):
    s = [0]*len(input[0].strip())
    h = int(len(input)/2)
    for l in input:
        for i, d in enumerate(l.strip()):
            if d == "1":
                s[i] += 1

    g, e = 0, 0
    for i, d in enumerate(reversed(s)):
        gb = 1 if d >= h else 0
        eb = 0 if d >= h else 1
        g += gb*(2**i)
        e += eb*(2**i)

    print(bin(g), bin(e))
    print(g, e, g*e)

one(ex)
one(input1)

import collections as coll

def get_mcd(l, i):
    c = coll.Counter([x[i] for x in l])
    (m, mc), (l, lc) = c.most_common()
    if mc == lc:
        return "1"
    return m

def get_lcd(l, i):
    c = coll.Counter([x[i] for x in l])
    (m, mc), (l, lc) = c.most_common()
    if mc == lc:
        return "0"
    return l

def find_o2(l):
    for i in range(len(l[0])):
        mcd = get_mcd(l, i)
        l = list(filter(lambda x: x[i] == mcd, l))
        if len(l) == 1:
            return l[0]

def find_co2(l):
    for i in range(len(l[0])):
        lcd = get_lcd(l, i)
        l = list(filter(lambda x: x[i] == lcd, l))
        if len(l) == 1:
            return l[0]

def two(input):
    o2 = find_o2(input)
    co2 = find_co2(input)
    print(o2, co2)
    print(int(o2, 2) * int(co2, 2))



print("=====two")
two(ex)
two(input1)
