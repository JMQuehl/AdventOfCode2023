import re
from collections import deque

import numpy.typing as npt
import numpy as np

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple

up = np.array((-1, 0))
down = np.array((1, 0))
left = np.array((0, -1))
right = np.array((0, 1))

direction_map = {
    tuple(up): {'|': up, '7': left, 'F': right},
    tuple(left): {'-': left, 'L': up, 'F': down},
    tuple(down): {'|': down, 'L': right, 'J': left},
    tuple(right): {'-': right, 'J': up, '7': down}}

blow_up_map = {'|': ('.', '|'), '-': ('-', '.'), 'L': ('-', '.'), 'J': ('.', '.'), '7': ('.', '|'), 'F': ('-', '|'),
               '.': ('.', '.')}


def get_loop_board(input_file_content: List[str]) -> npt.NDArray:
    """
    Creates a numpy NDArray which contains NaN at every position that is not part of the loop.
    For every position that is part of the loop, the array contains the distance from the starting position S.
    """
    board = np.empty((len(input_file_content), len(input_file_content[0].strip())))
    board[:] = np.nan
    cur_coord = np.array((0, 0))
    for i in range(len(input_file_content)):
        if 'S' in input_file_content[i]:
            cur_coord = (i, input_file_content[i].index('S'))
            board[cur_coord] = 0
            break
    loop_length = 1
    next_direction = up
    if cur_coord[0] > 0 and input_file_content[cur_coord[0] - 1][cur_coord[1]] in direction_map[tuple(up)]:
        cur_coord += up
        next_direction = direction_map[tuple(up)][input_file_content[cur_coord[0]][cur_coord[1]]]
    elif cur_coord[0] + 1 < len(input_file_content) and input_file_content[cur_coord[0] + 1][cur_coord[1]] in \
            direction_map[tuple(down)]:
        cur_coord += down
        next_direction = direction_map[tuple(down)][input_file_content[cur_coord[0]][cur_coord[1]]]
    elif cur_coord[1] > 0 < len(input_file_content) and input_file_content[cur_coord[0]][cur_coord[1] - 1] in \
            direction_map[tuple(left)]:
        cur_coord += left
        next_direction = direction_map[tuple(up)][input_file_content[cur_coord[0]][cur_coord[1]]]
    board[cur_coord[0]][cur_coord[1]] = 1
    while input_file_content[cur_coord[0]][cur_coord[1]] != 'S':
        loop_length += 1
        cur_coord += next_direction
        board[cur_coord[0]][cur_coord[1]] = loop_length
        if input_file_content[cur_coord[0]][cur_coord[1]] != 'S':
            next_direction = direction_map[tuple(next_direction)][input_file_content[cur_coord[0]][cur_coord[1]]]
    farthest = int(loop_length / 2)
    return np.vectorize(lambda x: min(x, (2 * farthest) - x) if not np.isnan(x) else np.nan)(board)


def blow_up(input_file_content: List[str]) -> List[str]:
    """
    Creates a new, larger board in which between all parallel lines there exists at least one empty space.
    Also there is an empty frame around the board in order to facilitate the filling-algorithm.
    """
    new_input = [''.join(['.'] * ((len(input_file_content[0])) * 2))]
    for line in input_file_content:
        line_list = ['.']
        next_line_list = ['.']
        for i, letter in enumerate(line.strip()):
            line_list.append(letter)
            if letter != 'S':
                line_list.append(blow_up_map[letter][0])
                next_line_list.append(blow_up_map[letter][1])
            else:
                if line_list[-2] == '.':
                    if new_input[-1][i] == '.':
                        # S = F
                        line_list.append('-')
                        next_line_list.append('|')
                    elif i + 1 < len(line.strip()) and line[i + 1] in '-7J':
                        # S = L
                        line_list.append('-')
                        next_line_list.append('.')
                    else:
                        # S = |
                        line_list.append('.')
                        next_line_list.append('|')
                else:
                    if new_input[-1][i] == '|':
                        # S = J
                        line_list.append('.')
                        next_line_list.append('.')
                    elif i + 1 < len(line.strip()) and line[i + 1] in '-7J':
                        # S = -
                        line_list.append('-')
                        next_line_list.append('.')
                    else:
                        # S = 7
                        line_list.append('.')
                        next_line_list.append('|')
            next_line_list.append('.')
        new_input.append(line_list)
        new_input.append(next_line_list)

    return new_input


def fill_board(board: npt.NDArray, value: int = 0, start: Tuple[int, int] = (0, 0)):
    """
    In a "blown up" board each empty space that is not inside the loop is reachable from (0,0).
    So by filling every NaN reachable this way with a number, all remaining NaNs are inside the loop.
    """
    to_fill = deque([start])
    while len(to_fill) > 0:
        cur_coords = to_fill.pop()
        board[cur_coords[0]][cur_coords[1]] = value
        if cur_coords[0] - 1 >= 0 and np.isnan(board[cur_coords[0] - 1][cur_coords[1]]):
            to_fill.append((cur_coords[0] - 1, cur_coords[1]))
        if cur_coords[0] + 1 < len(board) and np.isnan(board[cur_coords[0] + 1][cur_coords[1]]):
            to_fill.append((cur_coords[0] + 1, cur_coords[1]))
        if cur_coords[1] - 1 >= 0 and np.isnan(board[cur_coords[0]][cur_coords[1] - 1]):
            to_fill.append((cur_coords[0], cur_coords[1] - 1))
        if cur_coords[1] + 1 < len(board[0]) and np.isnan(board[cur_coords[0]][cur_coords[1] + 1]):
            to_fill.append((cur_coords[0], cur_coords[1] + 1))


class Task10(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The point farthest from the starting position in the loop starting with S is %d steps away."
        self.bonus_answer_text = "%d"
        self.task_number = 10

    def solve_task(self, input_file_content: List[str]) -> int:
        """
        we assume a coordinate system like this:
        __________> j
        |
        | i
        |
        V
        """
        board = get_loop_board(input_file_content)
        return int(np.nanmax(board))

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        """
        idea: double the size of the board so that spaces between parallel lines are created.
        Afterwards, mark all areas reachable from outside as not inside the loop and count the remaining ones.
        """
        board = get_loop_board(blow_up(input_file_content))
        fill_board(board)
        counter = 0
        for i in range(1, len(board), 2):
            for j in range(1, len(board[0]), 2):
                if np.isnan(board[i][j]):
                    counter += 1
        return counter

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('[|\-LJ7F.S]+\n?', line) for line in input_file_content)
