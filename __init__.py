from inspect import currentframe
from pathlib import Path

import pytest


def get_input(me=None):
    if me is None:
        me = Path(currentframe().f_back.f_code.co_filename)
    return Path(me.parent / "input" / f"{me.stem}.txt").read_text()


def solution(want_example, want_puzzle=None, run_puzzle=True):
    def decorator(fn):
        params = [pytest.param(want_example, id="example")]
        if run_puzzle:
            params.append(pytest.param(want_puzzle, id="puzzle"))

        @pytest.mark.parametrize("want", params)
        def wrapper(puzzle_input, want):
            got = fn(puzzle_input)
            if want is None:
                pytest.skip(f"unverified solution is {got}")
            else:
                assert want == got, f"{want} != {got}"

        return wrapper

    return decorator
