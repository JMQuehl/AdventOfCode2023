from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
import copy

direction_map = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
direction_order = ['north', 'west', 'south', 'east']


def shift_into_direction(board: List[List[str]], direction_key: str) -> List[List[str]]:
    stones = []
    direction = direction_map[direction_key]
    new_board = copy.deepcopy(board)
    for i, line in enumerate(new_board):
        for j, char in enumerate(line):
            if char == 'O':
                stones.append((i, j))
    if direction_key in ['south', 'east']:
        stones.reverse() # this is necessary since the default order of stones is top -> bottom, left -> right
    for stone in stones:
        while 0 <= stone[0] + direction[0] < len(new_board) and 0 <= stone[1] + direction[1] < len(new_board[0]) and \
                new_board[stone[0] + direction[0]][stone[1] + direction[1]] == '.':
            new_board[stone[0]][stone[1]] = '.'
            new_board[stone[0] + direction[0]][stone[1] + direction[1]] = 'O'
            stone = (stone[0] + direction[0], stone[1] + direction[1])
    return new_board


def evaluate_load(board: List[List[str]]) -> int:
    sum_of_load = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                sum_of_load += len(board) - i
    return sum_of_load


class Task14(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The total load on the north beam is: %d.'
        self.bonus_answer_text = 'After a billion cycles, the load on the north beam is: %d.'
        self.task_number = 14

    def solve_task(self, input_file_content: List[str]):
        board = [list(x.strip()) for x in input_file_content]
        board = shift_into_direction(board, 'north')
        return evaluate_load(board)

    def solve_bonus_task(self, input_file_content: List[str]):
        """
        Idea: After a while the board state repeats. So just save every board state and when it was found in order to
        find the cycle. Then just calculate how many cycles have to be done afterwards in order to get to 1000000000.
        """
        board = [list(x.strip()) for x in input_file_content]
        i = 0
        history = {}
        jumped = False
        while i < 4000000000:
            board = shift_into_direction(board, direction_order[i % len(direction_order)])
            i += 1
            if not jumped:
                hashed_board = hash("".join(["".join(x) for x in board]))
                if not hashed_board in history:
                    history[hashed_board] = i
                else:
                    i = 4000000000 - ((4000000000 - i) % (i - history[hashed_board]))
                    jumped = True
        return evaluate_load(board)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[O.#]+\n?", line) for line in input_file_content)
