import pytest


def solution(want_example, want_puzzle=None):
    def decorator(fn):
        @pytest.mark.parametrize(
            "want",
            [
                pytest.param(want_example, id="example"),
                pytest.param(want_puzzle, id="puzzle"),
            ],
        )
        def wrapper(puzzle_input, want):
            got = fn(puzzle_input)
            if want is None:
                pytest.skip(f"unverified solution is {got}")
            else:
                assert want == got, f"{want} != {got}"

        return wrapper

    return decorator
