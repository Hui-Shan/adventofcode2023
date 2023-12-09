import re

from read import get_input


class Sequence:
    def __init__(self, values: list):
        self.values = values
        self.subsequence = self.set_subsequence()

    def is_all_zero(self):
        return all([el == 0 for el in self.values])

    def set_subsequence(self):
        if not self.is_all_zero():
            if len(self.values) > 1:
                diffs = []
                for ii in range(1, len(self.values)):
                    diffs.append(self.values[ii] - self.values[ii - 1])
            else:
                diffs = [0]
            return Sequence(values=diffs)
        else:
            return None

    def get_prediction(self):
        if self.is_all_zero():
            pred = 0
        else:
            pred = self.subsequence.get_prediction()
        res = self.values[-1] + pred
        return res

    def get_backward_prediction(self):
        if self.is_all_zero():
            pred = 0
        else:
            pred = self.subsequence.get_backward_prediction()
        res = self.values[0] - pred
        return res

    def __str__(self):
        return " ".join([str(el) for el in self.values])


class Puzzle:
    def __init__(self, input: list):
        self.input = input

    def sum_extrapolated_value(self, forward: str = True) -> int:
        sum = 0
        for line in self.input:
            values = [int(el) for el in re.findall(r"-?\d+", line)]
            new_seq = Sequence(values)
            if forward:
                res = new_seq.get_prediction()
            else:
                res = new_seq.get_backward_prediction()
            sum += res

        return sum


if __name__ == "__main__":
    real_input = get_input(day=9)
    test_input = ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]

    test_puzzle = Puzzle(test_input)
    test_res1 = test_puzzle.sum_extrapolated_value()
    test_res2 = test_puzzle.sum_extrapolated_value(forward=False)

    real_puzzle = Puzzle(real_input)
    real_res1 = real_puzzle.sum_extrapolated_value()
    real_res2 = real_puzzle.sum_extrapolated_value(forward=False)

    print(f"Part 1 test: {test_res1}")
    print(f"Part 1 real: {real_res1}")

    print(f"Part 2 test: {test_res2}")
    print(f"Part 2 real: {real_res2}")
