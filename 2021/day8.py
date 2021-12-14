#!/usr/bin/python3

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.read()

ex = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

def parse(xin):
    for l in xin.split("\n"):
        if not l:
            continue
        a, b = l.strip().split(" | ")
        yield a.split(" "), b.split(" ")


segs = {k: set(list(v)) for k, v in {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}.items()}


def count_digits(xin, nums=[1, 4, 7, 8]):
    c = 0
    ok = [len(segs[n]) for n in nums]
    for _, o in parse(xin):
        for d in o:
            if len(d) in ok:
                c += 1
    print(c)


def decode_one(sigs, outs):
    known = {}

    for s in sigs:
        ls = len(s)
        ss = set(s)
        if ls == 2:
            known[1] = ss
        elif ls == 4:
            known[4] = ss
        elif ls == 3:
            known[7] = ss
        elif ls == 7:
            known[8] = ss
    for s in sigs:
        ls = len(s)
        ss = set(s)
        if ls == 5:
            if (known[4] - known[1]).issubset(ss):
                known[5] = ss
            elif known[1].issubset(ss):
                known[3] = ss
            else:
                known[2] = ss
        elif ls == 6:
            if known[4].issubset(ss):
                known[9] = ss
            elif known[1].issubset(ss):
                known[0] = ss
            else:
                known[6] = ss

    rev = {"".join(sorted(v)): k for k, v in known.items()}
    return int("".join(str(rev["".join(sorted(o))]) for o in outs))


def decode(xin):
    print(sum(decode_one(sigs, outs) for sigs, outs in parse(xin)))


count_digits(ex)
count_digits(in1)
print("===two")
decode(ex)
decode(in1)
