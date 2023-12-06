import re
from math import sqrt, ceil

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def parse_input(input_file_content: List[str]) -> (List[int], List[int]):
    return [int(x) for x in re.findall('\d+', input_file_content[0])], [int(x) for x in
                                                                        re.findall('\d+', input_file_content[1])]


def get_number_of_winning_times(time: int, distance: int) -> int:
    lower_bound = 0.5 * (time - sqrt((time * time) - 4 * distance))
    if ceil(lower_bound) == int(lower_bound):
        lower_bound += 1
    upper_bound = 0.5 * (time + sqrt((time * time) - 4 * distance))
    if ceil(upper_bound) == int(upper_bound):
        upper_bound -= 1
    return int(upper_bound) - ceil(lower_bound) + 1


class Task06(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The product of the number of ways you can win each race is: %d"
        self.bonus_answer_text = "You can win this single race in %d different ways."
        self.task_number = 6

    def solve_task(self, input_file_content: List[str]) -> int:
        times, distances = parse_input(input_file_content)
        time_product = 1
        for i in range(len(times)):
            time_product *= get_number_of_winning_times(times[i], distances[i])
        return time_product

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        times, distances = parse_input(input_file_content)
        time = int("".join(str(x) for x in times))
        distance = int("".join(str(x) for x in distances))
        return get_number_of_winning_times(time, distance)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('(Time:( +\d+)+\n?)|(Distance:( +\d+)+\n?)', line) for line in input_file_content)
