import re
from collections import deque

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task09(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of the extrapolations for each next value is: %d"
        self.bonus_answer_text = "The sum of the extrapolations for each previous value is: %d"
        self.task_number = 9

    def solve_task(self, input_file_content: List[str]) -> int:
        sum_of_extrapolations = 0
        for line in input_file_content:
            current_difference = [int(x) for x in re.findall('-?\d+', line)]
            differences = [current_difference]
            while any([x != 0 for x in current_difference]):
                current_difference = [j - i for i, j in zip(current_difference[:-1], current_difference[1:])]
                differences.append(current_difference)
            sum_of_extrapolations += sum([x[-1] for x in differences])
        return sum_of_extrapolations

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        sum_of_extrapolations = 0
        for line in input_file_content:
            current_difference = [int(x) for x in re.findall('-?\d+', line)]
            differences = [deque(current_difference)]
            while any([x != 0 for x in current_difference]):
                current_difference = [j - i for i, j in zip(current_difference[:-1], current_difference[1:])]
                differences.append(deque(current_difference))
            for i in range(1,len(differences)-1):
                differences[-(i+1)].appendleft(differences[-(i+1)][0] - differences[-i][0])
            sum_of_extrapolations += differences[0][0] - differences[1][0]
        return sum_of_extrapolations

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('-?\d+( -?\d+)*\n?', line) for line in input_file_content)
