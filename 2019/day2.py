#!/usr/bin/python3

from intcode import *

def intcode(prog):
    addr = 0
    while prog[addr] != 99:
        opcode = prog[addr]
        if prog[addr] == 1:  # ADD
            prog[prog[addr + 3]] = prog[prog[addr + 1]] + prog[prog[addr + 2]]
        elif prog[addr] == 2:  # MUL
            prog[prog[addr + 3]] = prog[prog[addr + 1]] * prog[prog[addr + 2]]
        i += 4
    return prog


def parse_prog(prog_str):
    return list(map(int, prog_str.split(',')))


def prog_str(prog):
    return ','.join(map(str, prog))


def assertEqual(start, want):
    print('='*80)
    # a = prog_str(intcode(parse_prog(a)))
    prog = IntCode(start)
    prog.run()
    got = str(prog.mem)
    print(prog.mem)
    assert_msg = '%s != %s' % (got, want)
    assert got == want, assert_msg


def run_tests():
    assertEqual('1,0,0,0,99', '2,0,0,0,99')
    assertEqual('2,3,0,3,99', '2,3,0,6,99')
    assertEqual('2,4,4,5,99,0', '2,4,4,5,99,9801')
    assertEqual('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99')
    print("PASS")
    print()
    print()


INPUT = (
    '1,0,0,3,'
    '1,1,2,3,'
    '1,3,4,3,'
    '1,5,0,3,'
    '2,1,10,19,'
    '1,9,19,23,'
    '1,13,23,27,'
    '1,5,27,31,'
    '2,31,6,35,'
    '1,35,5,39,'
    '1,9,39,43,'
    '1,43,5,47,'
    '1,47,5,51,'
    '2,10,51,55,'
    '1,5,55,59,'
    '1,59,5,63,'
    '2,63,9,67,'
    '1,67,5,71,'
    '2,9,71,75,'
    '1,75,5,79,'
    '1,10,79,83,'
    '1,83,10,87,'
    '1,10,87,91,'
    '1,6,91,95,'
    '2,95,6,99,'
    '2,99,9,103,'
    '1,103,6,107,'
    '1,13,107,111,'
    '1,13,111,115,'
    '2,115,9,119,'
    '1,119,6,123,'
    '2,9,123,127,'
    '1,127,5,131,'
    '1,131,5,135,'
    '1,135,5,139,'
    '2,10,139,143,'
    '2,143,10,147,'
    '1,147,5,151,'
    '1,151,2,155,'
    '1,155,13,0,'
    '99,'
    '2,14,0,0')


def restore():
    prog = parse_prog(INPUT)
    prog[1] = 12
    prog[2] = 2
    print(IntCode(prog_str(prog)).run())


def decode():
    for noun in range(100):
        for verb in range(100):
            prog = parse_prog(INPUT)
            prog[1], prog[2] = noun, verb
            if IntCode(prog_str(prog)).run() == 19690720:
                print('!'*80)
                print(noun, verb)
                return

def main():
    run_tests()
    # restore()
    # decode()


if __name__ == '__main__':
    main()
