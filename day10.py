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

        symbols = []
        for y, row in enumerate(input):
            symbol_row = []
            for x, symbol in enumerate(row):
                symbol_row.append(".")
                if symbol in list(Pipe.directions.keys()):
                    cur_pipe = Pipe(x=x, y=y, symbol=symbol)
                    self.pipe_dict[(x, y)] = cur_pipe
                    if symbol == "S":
                        self.start_pipe = cur_pipe
            symbols.append(symbol_row)
        self.symbol_map = symbols

    def solve_part1(self):
        moves = self.find_start_directions()
        start_loop_coords = [(self.start_pipe.x, self.start_pipe.y)] + [
            el["coord"] for el in moves[:1]
        ]
        end_coord = [el["coord"] for el in moves[1:]]
        loop_coords = []

        sorted_sources = sorted([el["source"] for el in moves])
        if sorted_sources == ["E", "W"]:
            start_symbol = "-"
        elif sorted_sources == ["N", "S"]:
            start_symbol = "|"
        else:
            if "S" in sorted_sources:
                if "W" in sorted_sources:
                    start_symbol = "J"
                elif "E" in sorted_sources:
                    start_symbol = "L"
            elif "N" in sorted_sources:
                if "E" in sorted_sources:
                    start_symbol = "7"
                elif "W" in sorted_sources:
                    start_symbol = "F"

        self.symbol_map[self.start_pipe.y][self.start_pipe.x] = start_symbol

        ii = 1
        while len(set(list([el["coord"] for el in moves]))) > 1:
            new_moves = []

            for move_dict in moves:
                coords = move_dict["coord"]
                cur_pipe = self.pipe_dict[coords]

                new_coords = cur_pipe.get_next_coord(source=move_dict["source"])
                new_source = Puzzle.mirror[cur_pipe.directions[move_dict["source"]]]
                new_moves.append({"source": new_source, "coord": new_coords})
                loop_coords.append(new_coords)

                # update_symbol map
                if ii == 1:
                    self.symbol_map[coords[1]][coords[0]] = self.pipe_dict[
                        (coords)
                    ].symbol
                self.symbol_map[new_coords[1]][new_coords[0]] = self.pipe_dict[
                    (new_coords)
                ].symbol

            ii += 1
            moves = new_moves
        self.loop_coords = (
            start_loop_coords
            + [el for idx, el in enumerate(loop_coords) if (idx % 2) == 0]
            + [el for idx, el in enumerate(loop_coords) if (idx % 2) == 1][::-1]
            + end_coord
        )  # close the loop

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

    def solve_part2(self):
        area = 0
        for i in range(len(self.loop_coords)):
            if i == 0:
                prev = self.loop_coords[-1]
            else:
                prev = self.loop_coords[i - 1]
            curr = self.loop_coords[i]

            area += prev[0] * curr[1] - prev[1] * curr[0]
        area = abs(area / 2)

        # Pick's theorem to calculate integer points inside
        # A = i + b/2 - 1
        # i = <area> - <length of path>/2 + 1 ???
        res = int(area - len(self.loop_coords) / 2 + 2)  # why does 2 work here?

        return res

    def __str__(self):
        return f"S: {self.start_pipe}"


if __name__ == "__main__":
    test_input = ["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."]
    test_input = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]
    test_input = [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "...........",
    ]
    test_input = [
        ".F----7F7F7F7F-7....",
        ".|F--7||||||||FJ....",
        ".||.FJ||||||||L7....",
        "FJL7L7LJLJ||LJ.L-7..",
        "L--J.L7...LJS7F-7L7.",
        "....F-J..F7FJ|L7L7L7",
        "....L7.F7||L7|.L7L7|",
        ".....|FJLJ|FJ|F7|.LJ",
        "....FJL-7.||.||||...",
        "....L---J.LJ.LJLJ...",
    ]

    test_puzzle = Puzzle(input=test_input)
    test_res1 = test_puzzle.solve_part1()
    test_res2 = test_puzzle.solve_part2()
    # print(test_res2)

    real_input = get_input(day=10)
    real_puzzle = Puzzle(input=real_input)
    real_res1 = real_puzzle.solve_part1()
    print(f"Part 1: {real_res1}")

    real_res2 = real_puzzle.solve_part2()
    print(f"Part 2: {real_res2}")
