#!/usr/bin/python

import collections

min_p = 264360
max_p = 746325


def try_one(p):
    p_str = str(p)
    c = collections.Counter(p_str)
    return len(p_str) == 6 and all(p_str[i] <= p_str[i+1] for i in range(5)) and any(v==2 for v in c.values())


def dtry_one(p):
    print(p, bool(try_one(p)))

dtry_one(111111)
dtry_one(223450)
dtry_one(123789)
dtry_one(123444)
dtry_one(112233)
dtry_one(111122)
dtry_one(112345)

matches = list(filter(None, map(try_one, range(min_p, max_p+1))))
print(len(matches))
