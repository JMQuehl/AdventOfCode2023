import re

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def solve_task_generic(input_file_content: List[str], weight: int = 1) -> int:
    """
    idea: find all galaxies and all rows/columns which are empty.
    For each pair of galaxies, calculate the distance and add weight * number of free rows and columns.
    """
    empty_rows = []
    empty_columns = []

    galaxies = []
    for i, row in enumerate(input_file_content):
        found = False
        for j, column in enumerate(input_file_content[i].strip()):
            if input_file_content[i][j] == '#':
                found = True
                galaxies.append((i, j))
        if not found:
            empty_rows.append(i)

    for i in range(len(input_file_content[0].strip())):
        if '#' not in [x[i] for x in input_file_content]:
            empty_columns.append(i)

    sum_of_distances = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sum_of_distances += abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
            sum_of_distances += weight * len(
                [x for x in range(min(galaxies[i][0], galaxies[j][0]) + 1, max(galaxies[i][0], galaxies[j][0])) if
                 x in empty_rows])
            sum_of_distances += weight * len(
                [x for x in range(min(galaxies[i][1], galaxies[j][1]) + 1, max(galaxies[i][1], galaxies[j][1])) if
                 x in empty_columns])

    return sum_of_distances


class Task11(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The galaxies are in sum %d units apart."
        self.bonus_answer_text = "For the older galaxies, they are in sum %d units apart."
        self.task_number = 11

    def solve_task(self, input_file_content: List[str]) -> int:
        return solve_task_generic(input_file_content)

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        return solve_task_generic(input_file_content, 999999)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('[.#]+\n?', line) for line in input_file_content)
