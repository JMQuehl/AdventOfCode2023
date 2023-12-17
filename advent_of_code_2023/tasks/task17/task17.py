import math
from collections import deque, defaultdict
from heapq import heappop, heappush

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def calculate_min_distance(min_steps, max_steps, grid, x=0):
    """
    Idea: use complex coordinates for position in order to enable efficient movement through the board.
    Instead of checking if over the step limit, just do all the allowed forward motion in that step but prohibit
    walking into the same direction as bevor by just calculating turn right and turn left.
    """
    end = [*grid][-1]
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()

    while todo:
        val, _, pos, dir = heappop(todo)

        if pos == end: return val
        if (pos, dir) in seen: continue
        seen.add((pos, dir))

        for d in 1j / dir, -1j / dir:
            for i in range(min_steps, max_steps + 1):
                if pos + d * i in grid:
                    v = sum(grid[pos + d * j] for j in range(1, i + 1))
                    heappush(todo, (val + v, (x := x + 1), pos + d * i, d))


class Task17(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'There will be a heat loss of at least: %d.'
        self.bonus_answer_text = 'The heat loss will be at least: %d.'
        self.task_number = 17

    def solve_task(self, input_file_content: List[str]):
        board = [x.strip() for x in input_file_content]
        distance_grid = {j + i * 1j: int(board[i][j]) for i in range(len(board)) for j in range(len(board[0]))}
        return calculate_min_distance(1, 3, distance_grid)

    def solve_bonus_task(self, input_file_content: List[str]):
        board = [x.strip() for x in input_file_content]
        distance_grid = {j + i * 1j: int(board[i][j]) for i in range(len(board)) for j in range(len(board[0]))}
        return calculate_min_distance(4, 10, distance_grid)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("\d+\n?", line) for line in input_file_content)
