#!/usr/bin/python3

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.readlines()

ex = "3,4,3,1,2"

def one(xin, days=80, debug=False):
    cur = [0]*9
    if debug:
        print(xin)
    for f in map(int, xin.split(",")):
        cur[f] += 1

    if debug:
        print(0, cur, sum(cur))

    for d in range(days):
        gen = [0]*9
        for i, r in enumerate(cur):
            if i == 0:
                gen[8] += r
                gen[6] += r
            else:
                gen[i-1] += r
        cur = gen
        if debug:
            print(d+1, cur, sum(cur))
    print(sum(cur))



one(ex)
one(in1[0])
print("===two")
one(ex, days=256)
one(in1[0], days=256)
