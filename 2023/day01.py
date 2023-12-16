from util import get_input


example = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def is_digit(n: str) -> bool:
    return ord(n) >= ord("1") and ord(n) <= ord("9")


def get_digit(n: str) -> int | None:
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for word, digit in digits.items():
        if n.endswith(word):
            return digit
    return None


def one():
    values = []
    for line in get_input():
        first, last = None, None
        for c in line:
            if is_digit(c):
                last = int(c)
                if first is None:
                    first = last
        values.append(10 * first + last)
    print(sum(values))


def two():
    values = []
    for line in get_input():
        first, last = None, None
        i, n = 0, 0
        while n < len(line):
            if is_digit(line[n]):
                last = int(line[n])
                if first is None:
                    first = last
                i = n
            elif (digit := get_digit(line[i : n + 1])) is not None:
                last = digit
                if first is None:
                    first = last
                i = n
            n += 1
        values.append(10 * first + last)
    print(sum(values))


one()
two()
