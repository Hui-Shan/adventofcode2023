import re

from read import get_input


class Mapping:
    def __init__(self, mapping_str: str):
        res = re.findall(r"\d+", mapping_str)
        dest, source, mrange = res[0], res[1], res[2]

        self.dest = int(dest)
        self.source = int(source)
        self.mrange = int(mrange)

    def maps_to_value(self, value_in) -> int:
        if self.source <= value_in < (self.source + self.mrange):
            return self.dest + (value_in - self.source)
        return None

    def __str__(self):
        return f"{self.dest} {self.source} {self.mrange}"


class Map:
    def __init__(self, map_str: list):
        self.name = map_str[0][:-1]
        self.mappings = []
        for line in map_str[1:]:
            new_mapping = Mapping(line)
            self.mappings.append(new_mapping)

    def map_value(self, value):
        res = value
        for mapping in self.mappings:
            cur_map = mapping.maps_to_value(value_in=value)
            if cur_map is not None:
                res = cur_map

        return res

    def __str__(self):
        return f"{self.name}\n {[str(el) for el in self.mappings]}"


class Puzzle:
    def __init__(self, input: list):
        self.seeds = None
        self.maps = []

        maps_divs = [idx + 1 for (idx, line) in enumerate(input) if line == ""] + [
            len(input)
        ]
        self.seeds = [int(el) for el in re.findall(r"\d+", input[0])]

        self.seed_ranges = self.get_seed_ranges()

        for ii, jj in zip(maps_divs[:-1], maps_divs[1:]):
            new_map = Map(map_str=input[ii : jj - 1])
            self.maps.append(new_map)

    def solve_part1(self):
        lowest_value = None
        for seed in self.seeds:
            value = seed
            for map in self.maps:
                value = map.map_value(value)

            if lowest_value is None or value < lowest_value:
                lowest_value = value

        return lowest_value

    def get_seed_ranges(self):
        n_ranges = int(len(self.seeds) / 2)
        range_list = []

        for ii in range(n_ranges):
            start = self.seeds[ii]
            end = self.seeds[2 * ii - 1]

            range_list.append((start, end - 1))
        return range_list

    def solve_part2(self):
        print("need to fix part 2")

    #     edges = [el for el in self.seed_ranges]
    #     for ii in range(int(len(self.seeds) / 2)):
    #         edges[2 * ii + 1] += edges[2 * ii]
    #
    #     lowest_value = None
    #     for seed in edges:
    #         value = seed
    #         for map in self.maps:
    #             value = map.map_value(value)
    #
    #         if lowest_value is None or value < lowest_value:
    #             lowest_value = value
    #
    #     return lowest_value

    def __str__(self):
        return f"{self.seeds}, {[str(map) for map in self.maps]}"


if __name__ == "__main__":
    real_input = get_input(day=5)
    test_input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    test_puzzle = Puzzle(input=test_input)
    res1_test = test_puzzle.solve_part1()
    print(f"Test res1: {res1_test}")

    real_puzzle = Puzzle(input=real_input)
    res1_real = real_puzzle.solve_part1()
    print(f"Real res1: {res1_real}")

    res2_test = test_puzzle.solve_part2()
    # print(test_puzzle)
    print(f"Test res2: {res2_test}")
