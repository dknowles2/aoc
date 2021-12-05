#!/usr/bin/python3

DEBUG = False

def Add(a, b, out):
    out.val = a.val + b.val
    return True


def Mul(a, b, out):
    out.val = a.val * b.val
    return True


def Save(a, out):
    out.val = a.val
    return True


def Term():
    return False


INSTRUCTIONS = {
    1: (Add, 3),
    2: (Mul, 3),
    3: (Save, 2),
    99: (Term, 0),
}

class Address(object):

    def __init__(self, addr, val):
        self.addr = addr
        self.val = val

    def __repr__(self):
        return '0x%02x{%s}' % (self.addr, self.val)


class Memory(object):

    def __init__(self, mem, ptr=0):
        self.ptr = ptr
        self.mem = [Address(i, v) for i, v in enumerate(mem)]

    def __str__(self):
        return ','.join(str(x.val) for x in self.mem)

    def get(self, addr):
        return self.mem[addr]

    def val(self, addr):
        return self.mem[addr].val

    def set(self, addr, val):
        self.mem[addr] = Address(addr, val)


class IntCode(object):

    def __init__(self, mem):
        self.mem = Memory(map(int, mem.split(',')))
        self.ptr = 0

    def run(self):
        keep_going = True
        while keep_going:
            keep_going = self.step()
        return self.mem.get(0).val

    def step(self):
        opcode = self.mem.val(self.ptr)
        op, n = INSTRUCTIONS[opcode]
        print([x for x in range(self.ptr+1, self.ptr+1+n)])
        ret = op(*(self.mem.get(x) for x in range(self.ptr+1, self.ptr+1+n)))
        self.ptr += n + 1
        return ret
