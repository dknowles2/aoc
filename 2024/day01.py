from heapq import heappop, heappush

from util import check, get_input, run

example = """\
3   4
4   3
2   5
1   3
3   9
3   3
""".splitlines


def one(input_fn=get_input):
    left: list[int] = []
    right: list[int] = []
    for line in input_fn():
        l, r = line.split()
        heappush(left, int(l))
        heappush(right, int(r))
    ret = 0
    while left:
        ret += abs(heappop(left) - heappop(right))
    return ret


def two(input_fn=get_input):
    left: list[str] = []
    right: dict[str, int] = {}
    for line in input_fn():
        l, r = line.split()
        left.append(l)
        if r not in right:
            right[r] = 0
        right[r] += 1
    return sum(right.get(n, 0) * int(n) for n in left)


run(one, example, 11, 1941353)
run(two, example, 31, 22539317)
