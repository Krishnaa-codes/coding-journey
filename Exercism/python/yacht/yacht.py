# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    if category == ONES:
        return dice.count(1)

    if category == TWOS:
        return dice.count(2) * 2

    if category == THREES:
        return dice.count(3) * 3

    if category == FOURS:
        return dice.count(4) * 4

    if category == FIVES:
        return dice.count(5) * 5

    if category == SIXES:
        return dice.count(6) * 6

    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
            
    if category == CHOICE:
        return sum(dice)

    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0

    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0

    if category == FOUR_OF_A_KIND:
        for number in range(1, 7):
            if dice.count(number) >= 4:
                return number * 4
        return 0

    if category == FULL_HOUSE:
        counts = []
        for num in set(dice):
            counts.append(dice.count(num))
        if sorted(counts) == [2, 3]:
            return sum(dice)
    return 0