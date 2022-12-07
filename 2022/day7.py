#!/usr/bin/python3

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


@dataclass
class Dir:

    name: str
    size: int = 0
    parent: Dir | None = None

    def add_file(self, name, fsize):
        d = self
        while d != None:
            d.size += fsize
            d = d.parent

    def add_dir(self, name):
        return Dir(name, parent=self)


def parse():
    cwd = Dir(name="/")
    dirs = [cwd]
    for l in get_input():
        if l.startswith("$ cd"):
            name = l.split()[-1]
            if name == "/":
                cwd = dirs[0]
            elif name == "..":
                cwd = cwd.parent
            else:
                dirs.append(cwd.add_dir(name))
                cwd = dirs[-1]
        elif l.startswith("$ ls") or l.startswith("dir "):
            continue
        else:
            size, name = l.split()
            cwd.add_file(name, int(size))
    return dirs


def one(dirs):
    print(sum([d.size for d in dirs if d.size <= 100000]))


def two(dirs):
    have_free = 70000000 - dirs[0].size
    need_to_free = 30000000 - have_free
    print(min([d.size for d in dirs if d.size > need_to_free]))


dirs = parse()
one(dirs)
two(dirs)
