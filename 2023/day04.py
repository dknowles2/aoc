from util import get_input


example = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines


def one(input_fn=get_input):
    score = 0
    for line in input_fn():
        _, numbers = line.split(": ")
        winners, mine = numbers.split(" | ")
        if (num_winners := len(set(mine.split()) & set(winners.split()))) > 0:
            score += 2 ** (num_winners - 1)
    print(score)


def two(input_fn=get_input):
    num_cards = {}
    for i, line in enumerate(input_fn()):
        if i not in num_cards:
            num_cards[i] = 0
        num_cards[i] += 1
        _, numbers = line.split(": ")
        winners, mine = numbers.split(" | ")
        num_winners = len(set(mine.split()) & set(winners.split()))
        for x in range(i + 1, i + 1 + num_winners):
            if x not in num_cards:
                num_cards[x] = 0
            num_cards[x] += num_cards[i]

    print(sum(num_cards.values()))


one()
two()
