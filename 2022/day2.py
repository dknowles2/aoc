#!/usr/bin/python3

import enum

def read_input():
    from os.path import basename
    with open("input/" + basename(__file__).replace(".py", ".txt")) as f:
        return f.readlines()

Hand = enum.Enum("Hand", ["ROCK", "PAPER", "SCISSORS"])
Result = enum.Enum("Result", ["LOSS", "DRAW", "WIN"])


def get_result(me, op):
    return {
        (Hand.ROCK, Hand.ROCK): Result.DRAW,
        (Hand.PAPER, Hand.PAPER): Result.DRAW,
        (Hand.SCISSORS, Hand.SCISSORS): Result.DRAW,
        (Hand.ROCK, Hand.SCISSORS): Result.WIN,
        (Hand.PAPER, Hand.ROCK): Result.WIN,
        (Hand.SCISSORS, Hand.PAPER): Result.WIN,
    }.get((me, op), Result.LOSS)


def get_score(me, result):
    score_map = {
        Hand.ROCK: 1,
        Hand.PAPER: 2,
        Hand.SCISSORS: 3,
        Result.LOSS: 0,
        Result.DRAW: 3,
        Result.WIN: 6,
    }
    return score_map[result] + score_map[me]


def one():
    trans = {
        "A": Hand.ROCK,
        "B": Hand.PAPER,
        "C": Hand.SCISSORS,
        "X": Hand.ROCK,
        "Y": Hand.PAPER,
        "Z": Hand.SCISSORS,
    }
    sc = 0
    for l in read_input():
        x, y = l.strip().split()
        op = trans[x]
        me = trans[y]
        res = get_result(me, op)
        sc += get_score(me, res)
    print(sc)



def get_hand(op, result):
    if result == Result.DRAW:
        return op
    if result == Result.WIN:
        return {
            Hand.ROCK: Hand.PAPER,
            Hand.PAPER: Hand.SCISSORS,
            Hand.SCISSORS: Hand.ROCK,
        }[op]
    # Loss
    return {
        Hand.ROCK: Hand.SCISSORS,
        Hand.PAPER: Hand.ROCK,
        Hand.SCISSORS: Hand.PAPER
    }[op]


def two():
    trans = {
        "A": Hand.ROCK,
        "B": Hand.PAPER,
        "C": Hand.SCISSORS,
        "X": Result.LOSS,
        "Y": Result.DRAW,
        "Z": Result.WIN,
    }
    sc = 0
    for l in read_input():
        x, y = l.strip().split()
        op = trans[x]
        res = trans[y]
        me = get_hand(op, res)
        sc += get_score(me, res)
    print(sc)


one()
print("===== two")
two()
