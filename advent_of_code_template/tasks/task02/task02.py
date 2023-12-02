import re

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def extract_max(color: str, input_str: str):
    return max(
        [int(color_string.removesuffix(' ' + color)) for color_string in re.findall('\d+ ' + color, input_str)])


class Task02(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of all ids of games that are possible with the given amount of cubes is: %d"
        self.bonus_answer_text = "The sum of the minimum power set is: %d"
        self.task_number = 2

    def solve_task(self, input_file_content: List[str]) -> int:
        id_sum = 0
        for line in input_file_content:
            game_id = int(re.findall('\d+', line)[0])
            max_red = extract_max('red', line)
            max_green = extract_max('green', line)
            max_blue = extract_max('blue', line)
            if max_red <= 12 and max_green <= 13 and max_blue <= 14:
                id_sum += game_id
        return id_sum

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        power_sum = 0
        for line in input_file_content:
            max_red = extract_max('red', line)
            max_green = extract_max('green', line)
            max_blue = extract_max('blue', line)
            power_sum += max_red * max_green * max_blue
        return power_sum

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('Game \d+: ([(\d+ green(, )?)(\d+ blue(, )?)(\d+ red(, )?)];?)+\n?', line) for line in
                   input_file_content)
