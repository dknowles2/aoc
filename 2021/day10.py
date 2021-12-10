#!/usr/bin/python3

with open("input/" + __file__.replace(".py", ".txt")) as f:
    in1 = f.readlines()

ex = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip().split("\n")

match = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}
rmatch = {v:k for k, v in match.items()}


def find_illegal_char(line):
    st = []
    for c in line.strip():
        if c in match:
            st.append(c)
        else:
            a = st.pop()
            if a != rmatch[c]:
                return c
    return None


def syntax_error_score(xin):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for l in xin:
        c = find_illegal_char(l)
        if c is not None:
            score += points[c]
    print(score)


def find_missing_end(line):
    st = []
    for c in line.strip():
        if c in match:
            st.append(c)
        elif c == match[st[-1]]:
            st.pop()
    return [match[c] for c in reversed(st)]


def incomplete_score(xin):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for l in xin:
        if find_illegal_char(l):
            continue
        s = 0
        for c in find_missing_end(l):
            s = (s * 5) + points[c]
        scores.append(s)
    print(sorted(scores)[int(len(scores)/2)])



syntax_error_score(ex)
syntax_error_score(in1)
print('====two')
incomplete_score(ex)
incomplete_score(in1)
