from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task00(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "%d"
        self.bonus_answer_text = "%d"
        self.task_number = 0

    def solve_task(self, input_file_content: List[str]):
        return -1

    def solve_bonus_task(self, input_file_content: List[str]):
        return -1

    def is_input_valid(self, input_file_content: List[str]):
        return True
