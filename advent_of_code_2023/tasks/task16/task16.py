from collections import deque

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re

up = 0
right = 1
down = 2
left = 3
direction_dict = {(1, 0): down, (0, 1): right, (-1, 0): up, (0, -1): left}

mirror_mapping = {(1, 0): {'.': [(1, 0)], '|': [(1, 0)], '\\': [(0, 1)], '/': [(0, -1)], '-': [(0, 1), (0, -1)]},
                  (0, 1): {'.': [(0, 1)], '|': [(1, 0), (-1, 0)], '\\': [(1, 0)], '/': [(-1, 0)], '-': [(0, 1)]},
                  (-1, 0): {'.': [(-1, 0)], '|': [(-1, 0)], '\\': [(0, -1)], '/': [(0, 1)], '-': [(0, 1), (0, -1)]},
                  (0, -1): {'.': [(0, -1)], '|': [(1, 0), (-1, 0)], '\\': [(-1, 0)], '/': [(1, 0)], '-': [(0, -1)]}}


def get_number_of_energized_tiles(obstacle_board: List[str], start: Tuple[Tuple[int, int], List[int]] = None):
    """
    Idea: Keep a map which contains all directions from which a tile was entered and exited in order to avoid looping endlessly.
    """
    if start is None:
        start = ((0, 1), [0, 0])
    light_board = [[[False] * 4 for _ in range(len(obstacle_board[0]))] for _ in range(len(obstacle_board))]
    light_board[start[1][0]][start[1][1]][direction_dict[(-start[0][0], -start[0][1])]] = True
    next_positions = deque([start])
    while next_positions:
        direction, current_position = next_positions.pop()
        possible_next_directions = mirror_mapping[direction][
            obstacle_board[current_position[0]][current_position[1]]]
        for x in possible_next_directions:
            if current_position[0] + x[0] in range(len(obstacle_board)) and current_position[1] + x[1] in range(
                    len(obstacle_board[0])) and not \
                    light_board[current_position[0] + x[0]][current_position[1] + x[1]][
                        direction_dict[(-x[0], -x[1])]]:
                # if not out of bounds and if the tile has neither been entered nor exited this way before.
                next_positions.append((x, [current_position[0] + x[0], current_position[1] + x[1]]))
                light_board[current_position[0] + x[0]][current_position[1] + x[1]][
                    direction_dict[(-x[0], -x[1])]] = True
    return sum([sum([int(any(column)) for column in line]) for line in
                light_board])  # counts each tile if it was entered or exited at least once.


class Task16(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'Starting in the top left corner, %d tiles are energized.'
        self.bonus_answer_text = 'The maximum number of tiles energized if starting in any possible position is: %d.'
        self.task_number = 16

    def solve_task(self, input_file_content: List[str]):
        obstacle_board = [x.strip() for x in input_file_content]
        return get_number_of_energized_tiles(obstacle_board)

    def solve_bonus_task(self, input_file_content: List[str]):
        """
        Brute forcing all possible solutions to task 1.
        Could be optimized by skipping each starting position from which a ray of light exited in any previous solutions.
        """
        obstacle_board = [x.strip() for x in input_file_content]
        current_max = 0
        for i in range(len(obstacle_board)):
            current_max = max(current_max, get_number_of_energized_tiles(obstacle_board, ((0, 1), [i, 0])))
            current_max = max(current_max,
                              get_number_of_energized_tiles(obstacle_board, ((0, -1), [i, len(obstacle_board[i]) - 1])))
        for i in range(len(obstacle_board[0])):
            current_max = max(current_max, get_number_of_energized_tiles(obstacle_board, ((1, 0), [0, i])))
            current_max = max(current_max,
                              get_number_of_energized_tiles(obstacle_board, ((-1, 0), [i, len(obstacle_board) - 1])))
        return current_max

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch(r"[.|\-\\/]+\n?", line) for line in input_file_content)
