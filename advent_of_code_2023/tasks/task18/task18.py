import numpy as np

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re

direction_map = {'U': np.array((-1, 0)), 'R': np.array((0, 1)), 'D': np.array((1, 0)), 'L': np.array((0, -1))}
hex_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def get_area(instructions: List[Tuple[Tuple[int, int], int]]) -> int:
    """
    Idea: use the shoelace formula in order to calculate the area.
    Since only the inner area is calculated, the length of the contour has to be added.
    """
    corners = [np.array((0, 0))]
    position = np.array((0, 0), dtype='int64')
    border_length = 1
    for direction, steps in instructions:
        position = position + steps * direction
        corners.append(position)
        border_length += steps

    area = 0
    for i in range(1, len(corners)):
        area += (corners[i - 1][1] + corners[i][1]) * (corners[i - 1][0] - corners[i][0])
    area = (abs(area) + border_length + 1) // 2
    return area


class Task18(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The lagoon can hold at most %d cubic meters of lava.'
        self.bonus_answer_text = 'After fixing the instructions, the lagoon will be able to hold a total of %d cubic meters of lava.'
        self.task_number = 18

    def solve_task(self, input_file_content: List[str]):
        instructions = []
        for line in input_file_content:
            direction = direction_map[line[0]]
            steps = int(re.search(r'\d+', line).group())
            instructions.append((direction, steps))
        return get_area(instructions)

    def solve_bonus_task(self, input_file_content: List[str]):
        instructions = []
        for line in input_file_content:
            direction = direction_map[hex_map[line.strip()[-2]]]
            steps = int(line.strip()[-7:-2], 16)
            instructions.append((direction, steps))
        return get_area(instructions)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch(r"[LRUD] \d+ \(#[a-f\d]+\)\n?", line) for line in input_file_content)
