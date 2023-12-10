from read import get_input


class Pipe:
    directions = {
        "-": {"E": "W", "W": "E"},
        "|": {"N": "S", "S": "N"},
        "L": {"E": "N", "N": "E"},
        "J": {"N": "W", "W": "N"},
        "7": {"W": "S", "S": "W"},
        "F": {"E": "S", "S": "E"},
        "S": {},
    }

    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.directions = Pipe.directions[self.symbol]

    def get_next_coord(self, source: str):
        dest = self.directions[source]
        next_x = self.x
        next_y = self.y
        if dest == "E":
            next_x += 1
        elif dest == "W":
            next_x -= 1
        elif dest == "N":
            next_y -= 1
        elif dest == "S":
            next_y += 1

        return next_x, next_y

    def __str__(self):
        return f"{self.symbol} at ({self.x}, {self.y})"


class Puzzle:
    mirror = {"E": "W", "W": "E", "N": "S", "S": "N"}

    def __init__(self, input: list):
        self.pipe_dict = {}
        self.start_pipe = None

        for y, row in enumerate(input):
            for x, symbol in enumerate(row):
                if symbol in list(Pipe.directions.keys()):
                    cur_pipe = Pipe(x=x, y=y, symbol=symbol)
                    self.pipe_dict[(x, y)] = cur_pipe
                    if symbol == "S":
                        self.start_pipe = cur_pipe

    def solve_part1(self):
        moves = self.find_start_directions()

        ii = 1
        while len(set(list([el["coord"] for el in moves]))) > 1:
            new_moves = []

            for move_dict in moves:
                coords = move_dict["coord"]
                cur_pipe = self.pipe_dict[coords]

                new_coords = cur_pipe.get_next_coord(source=move_dict["source"])
                new_source = Puzzle.mirror[cur_pipe.directions[move_dict["source"]]]
                new_moves.append({"source": new_source, "coord": new_coords})

            ii += 1
            moves = new_moves
        return ii

    def find_start_directions(self):
        start_directions = []
        for move_dir in ["N", "S", "W", "E"]:
            x = self.start_pipe.x
            y = self.start_pipe.y

            if move_dir == "N":
                source = "S"
                y -= 1
            elif move_dir == "S":
                source = "N"
                y += 1
            elif move_dir == "E":
                source = "W"
                x += 1
            elif move_dir == "W":
                source = "E"
                x -= 1

            if (x, y) in self.pipe_dict.keys():
                next_pipe = self.pipe_dict[(x, y)]
                if source in list(next_pipe.directions.keys()):
                    start_directions.append({"source": source, "coord": (x, y)})
        return start_directions

    def __str__(self):
        return f"S: {self.start_pipe}"


if __name__ == "__main__":
    # test_input = ["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."]
    # test_puzzle = Puzzle(input=test_input)
    # test_res1 = test_puzzle.solve_part1()

    real_input = get_input(day=10)
    real_puzzle = Puzzle(input=real_input)
    real_res1 = real_puzzle.solve_part1()

    print(f"Part 1: {real_res1}")
