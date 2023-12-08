from read import get_input


class Hand:
    type_rank = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card",
    ]

    def __init__(self, hand_str: str, with_jokers: bool = False):
        parts = hand_str.split(" ")
        self.cards = parts[0]
        self.bid = int(parts[1])

        self.hand_type = self.set_type(with_jokers=with_jokers)

        if with_jokers:
            self.card_rank = [
                "A",
                "K",
                "Q",
                "T",
                "9",
                "8",
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "J",
            ]
        else:
            self.card_rank = [
                "A",
                "K",
                "Q",
                "J",
                "T",
                "9",
                "8",
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
            ]

    @staticmethod
    def get_kind_from_counts(counts: dict):
        if counts == [5]:
            htype = "Five of a kind"
        elif counts == [4, 1]:
            htype = "Four of a kind"
        elif counts == [3, 2]:
            htype = "Full house"
        elif counts == [3, 1, 1]:
            htype = "Three of a kind"
        elif counts == [2, 2, 1]:
            htype = "Two pair"
        elif counts == [2, 1, 1, 1]:
            htype = "One pair"
        else:
            htype = "High card"

        return htype

    def __str__(self):
        return f"{[str(el) for el in self.cards]} {self.bid}"

    def set_type(self, with_jokers: bool = False):
        card_dict = {}
        for c in self.cards:
            c_str = str(c)
            if c_str in card_dict.keys():
                card_dict[c_str] += 1
            else:
                card_dict[c_str] = 1
        counts = list(card_dict.values())
        counts.sort(reverse=True)

        htype = Hand.get_kind_from_counts(counts=counts)

        if with_jokers and ("J" in self.cards):
            n_jokers = card_dict["J"]
            if htype == "Four of a kind":
                htype = "Five of a kind"
            elif htype == "Three of a kind":
                if n_jokers in [1, 3]:
                    htype = "Four of a kind"
            elif htype == "Full house":
                if n_jokers in [2, 3]:
                    htype = "Five of a kind"
            elif htype == "Two pair":
                if n_jokers == 2:
                    htype = "Four of a kind"
                elif n_jokers == 1:
                    htype = "Full house"
            elif htype == "One pair":
                if n_jokers in [1, 2]:
                    htype = "Three of a kind"
            elif htype == "High card":
                if n_jokers == 1:
                    htype = "One pair"

        return htype

    def __lt__(self, other: object):
        tidx_self = Hand.type_rank.index(self.hand_type)
        tidx_other = Hand.type_rank.index(other.hand_type)

        is_less_than = None
        if tidx_self < tidx_other:
            is_less_than = True
        elif tidx_self > tidx_other:
            is_less_than = False
        else:  # need to invoke second
            differs = False
            while not differs:
                for card_self, card_other in zip(self.cards, other.cards):
                    cidx_self = self.card_rank.index(card_self)
                    cidx_other = self.card_rank.index(card_other)

                    if cidx_self > cidx_other:
                        differs = True
                        is_less_than = False
                        break
                    elif cidx_self < cidx_other:
                        differs = True
                        is_less_than = True
                        break

        return is_less_than


def solve_parts(input: list, part: int):
    hand_list = []
    for line in input:
        if part == 1:
            new_hand = Hand(line)
        elif part == 2:
            new_hand = Hand(line, with_jokers=True)
        else:
            print("No valid part chosen!")
            break
        hand_list.append(new_hand)

    hand_list.sort(reverse=True)

    sum = 0
    for ii, hand_ii in enumerate(hand_list):
        sum += (ii + 1) * hand_ii.bid

    return sum


if __name__ == "__main__":
    test_input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
    real_input = get_input(day=7)

    for i in [1, 2]:
        test_res = solve_parts(input=test_input, part=i)
        real_res = solve_parts(input=real_input, part=i)

        print(f"Part {i}: {test_res} (test)")
        print(f"Part {i}: {real_res} (real)")
