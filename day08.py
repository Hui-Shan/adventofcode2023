import math
import re

from read import get_input


class Instruction:
    def __init__(self, input: list):
        split_idx = [idx for (idx, line) in enumerate(input) if line == ""][0]

        self.directions = "".join(input[:split_idx])
        dict_specs = input[split_idx + 1 :]

        self.nodes = {}
        for line in dict_specs:
            line.split(" = ")
            node_values = re.findall(r"([A-Z]{3})", line)
            key = node_values[0]
            left = node_values[1]
            right = node_values[2]
            self.nodes[key] = {"L": left, "R": right}

        self.final_dest = "ZZZ"

    def solve_part1(self):
        dest = "AAA"
        n = 0
        while dest != self.final_dest:
            direction = self.directions[n % len(self.directions)]
            dest = self.nodes[dest][direction]
            n = n + 1

        return n

    def solve_part2(self):
        multi_starts = [el for el in list(self.nodes.keys()) if el.endswith("A")]
        print(multi_starts)

        solutions = {}
        for start in multi_starts:
            n = 0
            dest = start
            while not dest.endswith("Z"):
                direction = self.directions[n % len(self.directions)]
                dest = self.nodes[dest][direction]
                n += 1

            n_to_first_z = n
            while not (dest.endswith("Z") and (n > n_to_first_z)):
                direction = self.directions[n % len(self.directions)]
                dest = self.nodes[dest][direction]
                n += 1

            n_to_next_z = n - n_to_first_z

            solutions[start] = {"first": n_to_first_z, "loop": n_to_next_z}

        loop_values = [el["first"] for el in solutions.values()]

        return math.lcm(*loop_values)


if __name__ == "__main__":
    real_input = get_input(day=8)
    test_input = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]

    test_inst = Instruction(test_input)
    test_res1 = test_inst.solve_part1()
    test_res2 = test_inst.solve_part2()

    real_inst = Instruction(real_input)
    real_res1 = real_inst.solve_part1()
    real_res2 = real_inst.solve_part2()

    print(f"Part 1: {test_res1} (test), {real_res1} (real)")
    print(f"Part 2: {test_res2} (test), {real_res2} (real)")
