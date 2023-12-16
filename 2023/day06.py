from util import check, get_input

example1 = """\
Time:      7  15   30
Distance:  9  40  200
""".splitlines


def count_better(time: int, best: int) -> int:
    b = 0
    for t in range(time):
        if ((time - t) * t) > best:
            b += 1
    return b


def one(input_fn=get_input):
    lines = input_fn()
    times = [int(n) for n in lines[0].split(":")[1].split()]
    bests = [int(n) for n in lines[1].split(":")[1].split()]
    ret = 1
    for time, best in zip(times, bests):
        ret *= count_better(time, best)
    return ret


def two(input_fn=get_input):
    lines = input_fn()
    time = int("".join(lines[0].split(":")[1].split()))
    best = int("".join(lines[1].split(":")[1].split()))
    return count_better(time, best)


check(one(example1), 288)
print(one())
check(two(example1), 71503)
print(two())
