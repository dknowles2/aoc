from aoc import solution
from pytest import fixture


@fixture
def example():
    return """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def get_paper(puzzle_input: str) -> set[tuple[int, int]]:
    paper = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                paper.add((x, y))
    return paper


def get_accessible(paper: set[tuple[int, int]]) -> set[tuple[int, int]]:
    accessible = set()
    for x, y in paper:
        adj = set()
        for pos in (
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ):
            if pos in paper:
                adj.add(pos)
        if len(adj) < 4:
            accessible.add((x, y))
    return accessible


@solution(13, 1569)
def one(puzzle_input):
    paper = get_paper(puzzle_input)
    return len(get_accessible(paper))


@solution(43, 9280)
def two(puzzle_input):
    paper = get_paper(puzzle_input)
    num_removed = 0
    accessible = get_accessible(paper)
    while accessible:
        paper -= accessible
        num_removed += len(accessible)
        accessible = get_accessible(paper)
    return num_removed
