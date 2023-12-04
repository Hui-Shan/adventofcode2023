import re

from read import get_input


class Number:
    def __init__(self, value: int, y: int, adj_coords: list):
        self.value = int(value)
        self.ycoord = y
        self.adjacent_coords = adj_coords


def solve_part1(input: list) -> int:
    ymax = len(input)
    xmax = len(input[0])

    sum = 0

    for y, line in enumerate(input):
        iters = re.finditer(r"\d+", line)

        for el in iters:
            value = el.group()
            span = el.span()

            xleft = max(0, span[0] - 1)
            xright = min(xmax - 1, span[1])
            xrange = range(xleft, xright + 1)

            ytop = y - 1
            ybottom = y + 1
            valid_coords = []
            if ytop >= 0:
                coords = [(ytop, ii) for ii in xrange]
                valid_coords.extend(coords)

            if ybottom < ymax:
                coords = [(ybottom, ii) for ii in xrange]
                valid_coords.extend(coords)

            if (xleft < span[0]) and (xleft >= 0):
                valid_coords.append((y, xleft))

            if (xright >= span[1]) and (xright < xmax - 1):
                valid_coords.append((y, xright))

            symbols = [
                input[jj][ii] for (jj, ii) in valid_coords if input[jj][ii] != "."
            ]

            if len(symbols) > 0:
                sum += int(value)

    return sum


def solve_part2(input: list) -> int:
    numbers = []

    ymax = len(input)
    xmax = len(input[0])

    for y, line in enumerate(input):
        iters = re.finditer(r"\d+", line)

        for el in iters:
            value = el.group()
            span = el.span()

            xleft = max(0, span[0] - 1)
            xright = min(xmax - 1, span[1])
            xrange = range(xleft, xright + 1)

            ytop = y - 1
            ybottom = y + 1
            valid_coords = []
            if ytop >= 0:
                coords = [(ytop, ii) for ii in xrange]
                valid_coords.extend(coords)

            if ybottom < ymax:
                coords = [(ybottom, ii) for ii in xrange]
                valid_coords.extend(coords)

            if (xleft < span[0]) and (xleft >= 0):
                valid_coords.append((y, xleft))

            if (xright >= span[1]) and (xright < xmax - 1):
                valid_coords.append((y, xright))

            new_num = Number(value=value, y=y, adj_coords=valid_coords)
            numbers.append(new_num)

    total_gear_ratio = 0
    for y, line in enumerate(input):
        for x, el in enumerate(line):
            if el == "*":
                adj_numbers = []
                for number in numbers:
                    if (y, x) in number.adjacent_coords:
                        adj_numbers.append(number)

                if len(adj_numbers) == 2:
                    gear_ratio = adj_numbers[0].value * adj_numbers[1].value
                    total_gear_ratio += gear_ratio
    return total_gear_ratio


if __name__ == "__main__":
    real_input = get_input(day=3)

    test_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    res1_test = solve_part1(input=test_input)
    res1_real = solve_part1(input=real_input)

    print(f"Part1 TEST: {res1_test}")
    print(f"Part1 REAL: {res1_real}")

    res2_test = solve_part2(input=test_input)
    res2_real = solve_part2(input=real_input)

    print(f"Part2 TEST: {res2_test}")
    print(f"Part2 REAL: {res2_real}")
