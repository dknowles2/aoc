#!/usr/bin/python3

with open("input/" + __file__.replace(".py", ".txt")) as f:
    input1 = f.readlines()

ex = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().split("\n")

def parse(t, cmds):
    ret = []
    for l in t:
        d, x = l.split()
        ret.append((cmds[d], int(x)))
    return ret

cmds1 = {
    "forward": lambda x: (x, 0),
    "down": lambda x: (0, x),
    "up": lambda x: (0, -1*x),
}

def one(input):
    h, d = 0, 0
    for c, x in parse(input, cmds1):
        xh, xd = c(d)
        h += xh
        d += xd
    print(h, d)
    print(h * d)

cmds2 = {
    "forward": lambda x, h, d, a: (h+x, d+ a*x, a),
    "down": lambda x, h, d, a: (h, d, a+x),
    "up": lambda x, h, d, a: (h, d, a-x),
}

def two(input):
    h, d, a = 0, 0, 0
    for c, x in parse(input, cmds2):
        h, d, a = c(x, h, d, a)
    print(h, d, a)
    print(h * d)


one(ex)
one(input1)

print("====two")
two(ex)
two(input1)
