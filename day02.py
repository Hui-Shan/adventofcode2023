from read import get_input


class Game:
    colors = ["red", "green", "blue"]

    def __init__(self, game_str):
        id_part, draw_part = game_str.split(":")

        self.id = int(id_part.split(" ")[-1])
        draws = draw_part.split(";")

        self.draw_dicts = []
        for draw in draws:
            draw_dict = {}
            for part in draw.split(","):
                num, color = part.strip().split(" ")
                draw_dict[color] = int(num)
            self.draw_dicts.append(draw_dict)

    def is_game_possible(self, configuration: dict):
        """Returns True if all draws are possible with the given configuration"""
        checks = [
            self.is_draw_possible(draw, configuration) for draw in self.draw_dicts
        ]

        return all(checks)

    @staticmethod
    def is_draw_possible(draw_dict: dict, configuration: dict):
        """Returns True if draw is possible with given configuration"""

        is_possible = True
        for key, val in draw_dict.items():
            is_possible = is_possible & (draw_dict[key] <= configuration[key])

        return is_possible

    def get_power(self):
        min_dict = {}
        for color in Game.colors:
            min_dict[color] = 0
        for draw_dict in self.draw_dicts:
            for key, val in draw_dict.items():
                if val > min_dict[key]:
                    min_dict[key] = val

        power = 1
        for val in min_dict.values():
            power *= val

        return power


if __name__ == "__main__":
    test_input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    real_input = get_input(day=2)

    config = {"red": 12, "green": 13, "blue": 14}

    # Get sum of ids, get power
    test_sum = 0
    test_power = 0
    for line in test_input:
        game_i = Game(line)
        if game_i.is_game_possible(configuration=config):
            test_sum += game_i.id
        test_power += game_i.get_power()

    real_sum = 0
    real_power = 0
    for line in real_input:
        game_i = Game(line)
        if game_i.is_game_possible(configuration=config):
            real_sum += game_i.id
        real_power += game_i.get_power()

    print(f"Result test part 1: {test_sum}")
    print(f"Result real part 1: {real_sum}")
    print(f"Result test part 2: {test_power}")
    print(f"Result real part 2: {real_power}")
