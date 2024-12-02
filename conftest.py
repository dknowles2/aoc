from pathlib import Path
from typing import Any

from pytest import FixtureRequest, fixture


@fixture
def puzzle_input(request: FixtureRequest, example: Any):
    if "example" in request.keywords:
        return example
    elif "puzzle" in request.keywords:
        me = Path(request.path)
        input_file = Path(me.parent / "input" / f"{me.stem.replace('test_', '')}.txt")
        return input_file.read_text().splitlines()
    request.raiseerror("unknown puzzle")
