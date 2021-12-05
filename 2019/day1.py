#!/usr/bin/python

import math


def fuel(mass):
    ret = math.floor(mass / 3) - 2
    if ret < 0:
        return 0
    return ret + fuel(ret)


def sum_input(input_f):
    modules = []
    with open(input_f) as f:
        for l in f:
            if not l:
                continue
            modules.append(int(l))
    return sum(map(fuel, modules))


def assertEqual(a, b):
    assert a == b, '%s != %s' % (a, b)

def main():
    assertEqual(fuel(14), 2)
    assertEqual(fuel(1969), 966)
    print(sum_input('input/day1'))
    print('pass')


if __name__ == '__main__':
    main()
