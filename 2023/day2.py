from functools import reduce
from pathlib import Path


def get_input(me=Path(__file__)):
    return Path(f"{me.parent}/input/{me.stem}.txt").read_text().splitlines()


example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def one():
    ret = 0
    for line in get_input():
        game, rolls = line.split(": ")
        game = int(game.split(" ")[1])
        max_rolls = {}
        for roll in rolls.split("; "):
            for group in roll.split(", "):
                n, color = group.split()
                max_rolls[color] = max(max_rolls.get(color, 0), int(n))
        if (
            max_rolls.get("red", 0) <= 12
            and max_rolls.get("green", 0) <= 13
            and max_rolls.get("blue", 0) <= 14
        ):
            ret += game
    print(ret)


def two():
    ret = 0
    for line in get_input():
        game, rolls = line.split(": ")
        game = int(game.split(" ")[1])
        max_rolls = {}
        for roll in rolls.split("; "):
            for group in roll.split(", "):
                n, color = group.split()
                max_rolls[color] = max(max_rolls.get(color, 0), int(n))
        ret += reduce(lambda x, y: x * y, max_rolls.values())
    print(ret)


one()
two()
