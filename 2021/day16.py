#!/usr/bin/python3

from functools import reduce
from operator import mul, gt, lt, eq

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read()


def parse(xin):
    return hex2bin(xin.strip())


def hex2bin(h):
    # int(h, 16) won't work because the puzzle expects every hex character to
    # output 4 bits of binary. So we do a manual conversion instead.
    conv = {
        'A': '1010', 'C': '1100', 'B': '1011', 'E': '1110',
        'D': '1101', 'F': '1111', '1': '0001', '0': '0000',
        '3': '0011', '2': '0010', '5': '0101', '4': '0100',
        '7': '0111', '6': '0110', '9': '1001', '8': '1000',
    }
    return ''.join(conv[c] for c in h)


def decode(bits, debug=False):
    blen = len(bits)
    v, bits = int(bits[:3], 2), bits[3:]
    t, bits = int(bits[:3], 2), bits[3:]
    ret = dict(v=v, t=t, sp=[])
    if t == 4:
        # literal value
        if debug:
            print(f'LITERAL v={v}')
        val_bits = ''
        while True:
            chunk, bits = bits[0:5], bits[5:]
            val_bits += chunk[1:]
            if chunk[0] == '0':
                break
        ret['val'] = int(val_bits, 2)
    else:
        # operator value
        if debug:
            print(f'OPERATOR v={v}')
        i, bits = bits[0], bits[1:]
        if i == '0':
            # total length in bits
            nbits = int(bits[:15], 2)
            pbits = bits[15:15+nbits]
            bits = bits[15+nbits:]
            if debug:
                print(f'  nbits={nbits}')
            while len(pbits) > 6:
                sp = decode(pbits)
                ret['sp'].append(sp)
                pbits = pbits[sp['bc']:]
        else:
            # number of sub-packets
            npacks, bits = int(bits[:11], 2), bits[11:]
            if debug:
                print(f'  npacks={npacks}')
            for i in range(npacks):
                if debug:
                    print(f'  sub={i}')
                sp = decode(bits)
                ret['sp'].append(sp)
                bits = bits[sp['bc']:]
    ret['bc'] = blen - len(bits)
    return ret


def sum_versions(p):
    v = p['v']
    for sp in p['sp']:
        v += sum_versions(sp)
    return v


def one(xin):
    return sum_versions(decode(parse(xin)))


def exe(p):
    return {
        0: lambda p: sum(exe(sp) for sp in p['sp']),
        1: lambda p: reduce(mul, [exe(sp) for sp in p['sp']]),
        2: lambda p: min(exe(sp) for sp in p['sp']),
        3: lambda p: max(exe(sp) for sp in p['sp']),
        4: lambda p: p['val'],
        5: lambda p: 1 if gt(*[exe(sp) for sp in p['sp']]) else 0,
        6: lambda p: 1 if lt(*[exe(sp) for sp in p['sp']]) else 0,
        7: lambda p: 1 if eq(*[exe(sp) for sp in p['sp']]) else 0,
    }[p['t']](p)


def two(xin):
    return exe(decode(parse(xin)))


def check(got, want):
    assert got == want, f'got {got}, want {want}'


# Part one:
check(one('8A004A801A8002F478'), 16)
check(one('620080001611562C8802118E34'), 12)
check(one('C0015000016115A2E0802F182340'), 23)
check(one('A0016C880162017C3686B18A3D4780'), 31)
print('one =', one(in1))


# Part two:
check(two('C200B40A82'), 3)
check(two('04005AC33890'), 54)
check(two('880086C3E88112'), 7)
check(two('CE00C43D881120'), 9)
check(two('D8005AC2A8F0'), 1)
check(two('F600BC2D8F'), 0)
check(two('9C005AC2F8F0'), 0)
check(two('9C0141080250320F1802104A08'), 1)
print('two =', two(in1))
