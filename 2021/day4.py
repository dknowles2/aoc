#!/usr/bin/python3

"""Initially written on an iPad in Antigua :-)"""

with open("input/" + __file__.replace(".py", ".txt")) as f:
    input1 = f.readlines()

ex = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".strip().split("\n")

def parse(input):
    nums = map(int, input[0].strip().split(","))

    boards = []
    for i, line in enumerate(input[1:]):
        r = i % 6
        if r == 0:
            boards.append([set() for _ in range(11)])
            continue
        board = boards[-1]
        for j, n in enumerate(map(int, line.split())):
            board[0].add(n) # all nums
            board[r].add(n) # row
            board[6+j].add(n) # col
    return nums, boards

def play(input):
    nums, boards = parse(input)
    c = set()
    w = []
    for n in nums:
        c.add(n)
        for i, b in enumerate(boards[:]):
            if b is None:
                continue
            s = check(b, c, n)
            if s is not None:
                w.append(s)
                boards[i] = None
    return w

def check(b, c, n):
    for s in b[1:]:
        if len(s - c) == 0:
            return sum(b[0]-c)*n

def one(input):
    print(play(input)[0])

def two(input):
    print(play(input)[-1])

print("===one")
one(ex)
one(input1)

print("===two")
two(ex)
two(input1)
