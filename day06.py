import math
import numpy as np
import re


from read import get_input


def solve_abc(a: int, b: int, c: int) -> tuple:
    """Solve abc equation and return both solutions in a list"""

    D = np.sqrt(b**2 - (4 * a * c))

    x1 = (-b - D) / (2 * a)
    x2 = (-b + D) / (2 * a)

    sols = [x1, x2]
    sols.sort()

    return sols


class Race:
    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance

    def get_n_ways_to_beat(self):
        [t_min, t_max] = solve_abc(a=1, b=-self.time, c=self.distance)

        # round the solution appropriately to integer numbers
        if t_min % 1 == 0:
            t_min += 1
        else:
            t_min = int(math.ceil(t_min))
        if t_max % 1 == 0:
            t_max -= 1
        else:
            t_max = int(math.floor(t_max))

        n = int(t_max - t_min + 1)

        return n


class Competition:
    def __init__(self, input: list):
        for line in input:
            values = [int(el) for el in re.findall(r"\d+", line)]
            if line.startswith("Time"):
                self.times = values
                self.mega_time = int(line.split(":")[-1].replace(" ", ""))
            elif line.startswith("Distance"):
                self.distances = values
                self.mega_dist = int(line.split(":")[-1].replace(" ", ""))

        self.races = []
        for time, dist in zip(self.times, self.distances):
            new_race = Race(time=time, distance=dist)
            self.races.append(new_race)

        self.mega_race = Race(time=self.mega_time, distance=self.mega_dist)

    def solve_part1(self):
        res = 1
        for race in self.races:
            res *= race.get_n_ways_to_beat()
        return res

    def solve_part2(self):
        return self.mega_race.get_n_ways_to_beat()

    def __str__(self):
        return f"{self.times}, {self.distances}"


if __name__ == "__main__":
    real_input = get_input(day=6)
    test_input = ["Time:      7  15   30", "Distance:  9  40  200"]

    test_comp = Competition(test_input)
    real_comp = Competition(real_input)

    test_res1 = test_comp.solve_part1()
    print(f"Res1 TEST: {test_res1}")
    real_res1 = real_comp.solve_part1()
    print(f"Res1 REAL: {real_res1}")
    test_res2 = test_comp.solve_part2()
    print(f"Res2 TEST: {test_res2}")
    real_res2 = real_comp.solve_part2()
    print(f"Res2 REAL: {real_res2}")
