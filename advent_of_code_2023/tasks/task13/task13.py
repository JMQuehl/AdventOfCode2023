import math

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


def compare_boards(original: List[str], flipped: List[str]) -> int:
    """
    Returns the number of differences between two boards.
    """
    return sum(sum([original[i][j] != flipped[i][j] for j in range(len(original[i]))]) for i in range(len(original)))


def solve(input_file_content: List[str], target: int = 0):
    """
    Idea: Flip the board along each possible axes and compare the overlapping areas. If the number of differences
    between the two boards is the target number, use the axis for result calculation.
    """
    current_board = []
    boards = []
    for line in input_file_content:
        if not line.strip() == '':
            current_board.append(line.strip())
        else:
            boards.append(current_board)
            current_board = []
    boards.append(current_board)
    sum_of_codes = 0
    for board in boards:
        length = len(board)
        for i in range(1, len(board)):
            if compare_boards(board[max(0, 2 * i - length):2 * i],
                              board[min(-(length - (2 * i) + 1), -1):-(1 + (2 * length - 2 * i)):-1]) == target:
                sum_of_codes += 100 * i
                break
        length = len(board[0])
        for i in range(1, length):
            if compare_boards([x[max(0, 2 * i - length):2 * i] for x in board],
                              [x[min(-(length - (2 * i) + 1), -1):-(1 + (2 * length - 2 * i)):-1] for x in
                               board]) == target:
                sum_of_codes += i
                break
    return sum_of_codes


class Task13(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'After summarizing all notes, you get: %d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 13

    def solve_task(self, input_file_content: List[str]):
        return solve(input_file_content)

    def solve_bonus_task(self, input_file_content: List[str]):
        # Since the smudge will appear twice, we are looking for boards with a difference of 2.
        return solve(input_file_content, 2)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[#.]*\n?", line) for line in input_file_content)
