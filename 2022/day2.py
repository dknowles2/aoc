#!/usr/bin/python3


def read_input():
    from pathlib import Path

    me = Path(__file__)
    return Path(me.parent / "input" / (me.stem + ".txt")).read_text().splitlines()


ROCK, PAPER, SCISSORS = "A", "B", "C"
LOSS, DRAW, WIN = "X", "Y", "Z"
HAND_SCORE = {ROCK: 1, PAPER: 2, SCISSORS: 3}
RESULT_SCORE = {LOSS: 0, DRAW: 3, WIN: 6}


def one():
    trans = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
    winning_hands = {(ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER)}
    sc = 0
    for l in read_input():
        op, me = l.strip().split()
        me = trans[me]
        if me == op:
            res = DRAW
        else:
            res = WIN if (me, op) in winning_hands else LOSS
        sc += HAND_SCORE[me] + RESULT_SCORE[res]
    print(sc)


def two():
    sc = 0
    for l in read_input():
        op, res = l.strip().split()
        if res == DRAW:
            me = op
        else:
            me = {
                WIN: {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK},
                LOSS: {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER},
            }[res][op]
        sc += HAND_SCORE[me] + RESULT_SCORE[res]
    print(sc)


one()
two()
