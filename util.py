from inspect import currentframe
from pathlib import Path


def check(a, b):
    assert a == b, f"{a} != {b}"


def get_input():
    me = Path(currentframe().f_back.f_code.co_filename)
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()
