import re

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task13(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "%d"
        self.bonus_answer_text = "%d"
        self.task_number = 13

    def solve_task(self, input_file_content: List[str]) -> int:
        return -1

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        return -1

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('', line) for line in input_file_content)
