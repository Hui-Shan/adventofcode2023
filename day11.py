import itertools

from read import get_input


class Galaxy:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def get_manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        return f"#{self.id} ({self.x}, {self.y})"


class Image:
    def __init__(self, data: list):
        self.data = data

        self.empty_rows = self.get_empty_rows()
        self.empty_columns = self.get_empty_columns()
        self.expansion = self.expand()

        self.galaxies = self.get_galaxies()

    def expand(self) -> list:
        # horizontally
        dummy = []
        for ii, row in enumerate(self.data):
            row_str = "".join(row)
            dummy.append(row_str)
            if ii in self.empty_rows:
                dummy.append(row_str)

        # vertically
        new_dummy = [
            "".join(
                [
                    el + el if jj in self.empty_columns else el
                    for (jj, el) in enumerate(row)
                ]
            )
            for row in dummy
        ]

        return new_dummy

    def get_galaxies(self):
        ii = 0
        galaxy_list = []
        for y, row in enumerate(self.expansion):
            for x, val in enumerate(row):
                if val == "#":
                    new_galaxy = Galaxy(id=ii, x=x, y=y)
                    galaxy_list.append(new_galaxy)
                    ii += 1
        return galaxy_list

    def get_empty_rows(self):
        row_indices = []
        for idx, row in enumerate(self.data):
            if set(row) == set("."):
                row_indices.append(idx)

        return row_indices

    def get_empty_columns(self):
        col_indices = []
        for idx in range(len(self.data[0])):
            columns = [self.data[jj][idx] for jj in range(len(self.data))]
            if set(columns) == set("."):
                col_indices.append(idx)
        return col_indices

    def solve_part1(self):
        res = 0
        galaxy_pairs = [list(x) for x in itertools.combinations(self.galaxies, 2)]
        for pair in galaxy_pairs:
            dist = pair[0].get_manhattan_distance(pair[1])
            res += dist

        return res

    def __str__(self):
        return f"{[str(el) for el in self.galaxies]}"


class BigImage:
    def __init__(self, data: list, factor: int = 2):
        self.data = data

        self.empty_rows = self.get_empty_rows()
        self.empty_columns = self.get_empty_columns()

        self.factor = factor

        self.galaxies = self.get_galaxies()

    def get_galaxies(self):
        ii = 0
        galaxy_list = []
        for y, row in enumerate(self.data):
            for x, val in enumerate(row):
                if val == "#":
                    new_galaxy = Galaxy(id=ii, x=x, y=y)
                    galaxy_list.append(new_galaxy)
                    ii += 1
        return galaxy_list

    def get_empty_rows(self):
        row_indices = []
        for idx, row in enumerate(self.data):
            if set(row) == set("."):
                row_indices.append(idx)

        return row_indices

    def get_empty_columns(self):
        col_indices = []
        for idx in range(len(self.data[0])):
            columns = [self.data[jj][idx] for jj in range(len(self.data))]
            if set(columns) == set("."):
                col_indices.append(idx)
        return col_indices

    def solve_part2(self):
        res = 0
        galaxy_pairs = [list(x) for x in itertools.combinations(self.galaxies, 2)]
        for pair in galaxy_pairs:
            min_x = min(pair[0].x, pair[1].x)
            max_x = max(pair[0].x, pair[1].x)
            min_y = min(pair[0].y, pair[1].y)
            max_y = max(pair[0].y, pair[1].y)

            n_empty_cols = 0
            for col_idx in self.empty_columns:
                if min_x < col_idx < max_x:
                    n_empty_cols += 1
            n_empty_rows = 0
            for row_idx in self.empty_rows:
                if min_y < row_idx < max_y:
                    n_empty_rows += 1

            dist_x = n_empty_cols * (self.factor - 1) + abs(pair[0].x - pair[1].x)
            dist_y = n_empty_rows * (self.factor - 1) + abs(pair[0].y - pair[1].y)

            dist = dist_x + dist_y

            res += dist

        return res

    def __str__(self):
        return f"{[str(el) for el in self.galaxies]}"


if __name__ == "__main__":
    real_input = get_input(day=11)
    test_input = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]

    test_image = Image(data=test_input)
    res1_test = test_image.solve_part1()
    print(f"Part 1 (test): {res1_test}")

    real_image = Image(data=real_input)
    res1_real = real_image.solve_part1()
    print(f"Part 1 (real): {res1_real}")

    test_image = BigImage(data=test_input, factor=100)
    res2_test = test_image.solve_part2()
    print(f"Part 2 (test), with factor 100: {res2_test}")

    real_image = BigImage(data=real_input, factor=1000000)
    res2_real = real_image.solve_part2()
    print(f"Part 2 (real), factor one million: {res2_real}")
