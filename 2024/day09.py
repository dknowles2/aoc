from dataclasses import dataclass

from aoc import solution
from pytest import fixture


@fixture
def example():
    return "2333133121414131402"


@dataclass
class Node:
    start: int
    length: int
    id_num: int | None


@solution(1928, 6291146824486)
def one(puzzle_input):
    nodes: list[Node] = []
    start = 0
    for i, length in enumerate(map(int, puzzle_input.strip())):
        id_num = None
        if i % 2 == 0:
            id_num = i // 2
        nodes.append(Node(start, length, id_num))
        start += length

    checksum = 0
    while nodes:
        node = nodes.pop(0)
        if node.id_num is not None:
            for i in range(node.start, node.start + node.length):
                checksum += i * node.id_num
        else:
            i = 0
            while nodes and i < node.length:
                end = nodes.pop()
                if end.id_num is None:
                    continue
                checksum += (node.start + i) * end.id_num
                end.length -= 1
                if end.length > 0:
                    nodes.append(end)
                i += 1
    return checksum


@solution(2858, 6307279963620)
def two(puzzle_input):
    files: list[Node] = []
    holes: list[Node] = []
    start = 0
    for i, length in enumerate(map(int, puzzle_input.strip())):
        if i % 2 == 0:
            files.append(Node(start, length, i // 2))
        else:
            holes.append(Node(start, length, None))
        start += length

    checksum = 0
    while files:
        file = files.pop()
        for i, hole in enumerate(holes[:]):
            if hole.start > file.start:
                break
            if hole.length >= file.length:
                file.start = hole.start
                hole.start += file.length
                hole.length -= file.length
                if hole.length == 0:
                    holes.pop(i)
                break
        for i in range(file.start, file.start + file.length):
            checksum += i * file.id_num
    return checksum
