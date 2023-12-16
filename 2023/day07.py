from collections import Counter

from util import get_input

example = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines


def hand_type(hand, jokers=False):
    cnt = Counter(hand)
    j = 0
    if jokers and cnt.get("J", 0) < 5:
        j = cnt.pop("J", 0)

    c = [c for _, c in cnt.most_common()]
    # Add the jokers to the largest set
    c[0] += j

    if c[0] == 5:
        return 6  # 5 of a kind
    if c[0] == 4:
        return 5  # 4 of a kind
    if c[0] == 3:
        if c[1] == 1:
            return 3  # 3 of a kind
        return 4  # Full house
    if c[0] == 2:
        if c[1] == 2:
            return 2  # 2 pair
        return 1  # 1 pair
    return 0  # High card


def score(hand, jokers=False):
    cards = "J23456789TQKA" if jokers else "23456789TJQKA"
    items = [hand_type(hand, jokers)] + list(map(cards.index, hand))
    return items, sum(items[i] << ((len(items) - i) * 4) for i in range(len(items)))


def solve(input_fn=get_input, jokers=False):
    hands = []
    for line in input_fn():
        hand, bet = line.split()
        i, s = score(hand, jokers=jokers)
        hands.append((s, hand, int(bet)))
    hands.sort()
    print(sum((i + 1) * bet for i, (_, _, bet) in enumerate(hands)))


solve()
solve(jokers=True)
