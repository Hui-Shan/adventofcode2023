import re

from read import get_input


class Card:
    def __init__(self, card_str: str):
        (card, numbers) = card_str.split(": ")

        self.id = int(re.search(r"\d+", card).group())
        parts = numbers.split(" | ")

        self.winning_numbers = [int(el) for el in re.findall(r"\d+", parts[0])]
        self.your_numbers = [int(el) for el in re.findall(r"\d+", parts[1])]

    def get_number_of_matches(self):
        matches = [num for num in self.your_numbers if num in self.winning_numbers]
        return len(matches)

    def get_points(self):
        n_match = self.get_number_of_matches()
        if n_match == 0:
            return 0
        else:
            return 2 ** (n_match - 1)

    def __str__(self):
        return f"Card #{self.id} {self.winning_numbers} ({self.your_numbers})"


def solve_part1(input: list):
    total_points = 0
    for line in input:
        new_card = Card(line)
        total_points += new_card.get_points()

    return total_points


def solve_part2(input: list):
    card_dict = {}
    for ii, _ in enumerate(input):
        card_dict[ii + 1] = 1

    for ii, line in enumerate(input):
        new_card = Card(line)
        n_won_cards = new_card.get_number_of_matches()

        for jj in range(new_card.id + 1, new_card.id + n_won_cards + 1):
            card_dict[jj] += card_dict[new_card.id]

    return sum(card_dict.values())


if __name__ == "__main__":
    real_input = get_input(day=4)
    test_input = [
        "Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    res1_test = solve_part1(input=test_input)
    res1_real = solve_part1(input=real_input)

    print(f"Res 1 TEST: {res1_test}")
    print(f"Res 1 REAL: {res1_real}")

    res2_test = solve_part2(input=test_input)
    res2_real = solve_part2(input=real_input)

    print(f"Res 2 TEST: {res2_test}")
    print(f"Res 2 REAL: {res2_real}")
