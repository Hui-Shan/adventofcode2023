import re

from read import get_input


def get_first_and_last_index(line: str, value: str) -> int:
    """Returns first and last index of a value in a string. None if not occuring"""

    matches = [m.start(0) for m in re.finditer(str(value), line)]

    if matches:
        first_index = matches[0]
        last_index = matches[-1]
    else:
        first_index = None
        last_index = None

    return first_index, last_index


def get_number1(line: str):
    """Get number by adding first and last digits in string"""

    all_digits = [el for el in line if el.isdigit()]

    return int(all_digits[0] + all_digits[-1])


def get_number2(
    line: str,
    values: list = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ],
):
    """Get number by adding first and last number in string"""

    first_index = len(line)
    last_index = -1
    first_digit = ""
    last_digit = ""

    for val in values:
        str_val = str(val)
        cur_fidx, cur_lidx = get_first_and_last_index(line, str_val)

        if cur_fidx is not None and cur_fidx < first_index:
            first_index = cur_fidx
            first_digit = str_val

        if cur_lidx is not None and cur_lidx > last_index:
            last_index = cur_lidx
            last_digit = str_val

    rep_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digit_sum = first_digit + last_digit
    for key, dig in rep_dict.items():
        digit_sum = digit_sum.replace(key, dig)

    return digit_sum


def get_sum_calibration_values(input: list, part: int) -> int:
    cvalues = []
    for line in input:
        if part == 1:
            val = get_number1(line)
        else:
            val = get_number2(line)
        cvalues.append(int(val))
    return sum(cvalues)


if __name__ == "__main__":
    test_input1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    real_input = get_input(day=1)

    # part 1
    res1_test = get_sum_calibration_values(test_input1, part=1)
    print(f"Test result part 1: {res1_test}")

    res1_real = get_sum_calibration_values(real_input, part=1)
    print(f"Real result part 1: {res1_real}")

    # part 2
    test_input2 = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    res2_test = get_sum_calibration_values(test_input2, part=2)
    print(f"Test result part 2: {res2_test}")

    res2_real = get_sum_calibration_values(real_input, part=2)
    print(f"Real result part 2: {res2_real}")

    # TODO: clean up code
