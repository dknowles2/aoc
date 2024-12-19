from pathlib import Path
from typing import Any

from pytest import FixtureLookupError, FixtureRequest, fixture

from . import get_input


@fixture
def example_wrapper(request: FixtureRequest):
    try:
        return request.getfixturevalue("example")
    except FixtureLookupError:
        pass
    for test_name in request.keywords:
        break
    if test_name.startswith("one["):
        return request.getfixturevalue("example1")
    elif test_name.startswith("two["):
        return request.getfixturevalue("example2")
    raise FixtureLookupError


@fixture
def puzzle_input(request: FixtureRequest, example_wrapper: Any):
    if "example" in request.keywords:
        return example_wrapper
    elif "puzzle" in request.keywords:
        return get_input(Path(request.path))
    request.raiseerror("unknown puzzle")
