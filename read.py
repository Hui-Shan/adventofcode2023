def get_input(day: int) -> list:
    """Returns user input for <day> as list of lines"""

    input_file = f"inputs/input{str(day).zfill(2)}.txt"
    with open(input_file, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]
