from itertools import pairwise

from util import check, get_input


example1 = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".splitlines


def one(input_fn=get_input):
    ret = 0
    for line in input_fn():
        diff = [int(n) for n in line.split()]
        z = False
        pred = diff[-1]
        while not z:
            z = True
            ndiff = []
            for a, b in pairwise(diff):
                r = b - a
                ndiff.append(r)
                z &= r == 0
            pred += ndiff[-1]
            diff = ndiff
        ret += pred
    return ret


def two(input_fn=get_input):
    ret = 0
    for line in input_fn():
        diff = [int(n) for n in line.split()]
        z = False
        firsts = [diff[0]]
        while not z:
            z = True
            ndiff = []
            for a, b in pairwise(diff):
                r = b - a
                ndiff.append(r)
                z &= r == 0
            firsts.append(ndiff[0])
            diff = ndiff
        prev = 0
        for n in reversed(firsts):
            prev = n - prev
        ret += prev

    return ret


check(one(example1), 114)
print(one())
check(two(example1), 2)
print(two())
