from inspect import currentframe
from pathlib import Path

_RED = "\033[91m"
_GREEN = "\033[92m"
_RESET = "\033[0m"


def run(fn, get_example_input, example_want, final_want=None):
    f_name = fn.__name__
    print_result(f"{f_name} (example)", fn(get_example_input), example_want)
    get_final_input = lambda: get_input(lambda: currentframe().f_back.f_back)  # noqa
    print_result(f"{f_name} (final)  ", fn(get_final_input), final_want)


def print_result(name, got, want):
    if want is None:
        print(f"{name}: {got}")
        return
    result_str = f"{_GREEN}PASS" if want == got else f"{_RED}FAIL"
    cmp = "==" if want == got else "!="
    print(f"{name}: {result_str}{_RESET} ({got} {cmp} {want})")


def check(got, want):
    if got == want:
        message = "PASS"
        color = _GREEN
        cmp = "=="
    else:
        message = "FAIL"
        color = _RED
        cmp = "!="
    print(f"{color}{message}:{_RESET} {got} {cmp} {want}")


def get_input(get_frame=currentframe):
    me = Path(get_frame().f_back.f_code.co_filename)
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()
