from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task11.task11 import Task11, solve_task_generic
from advent_of_code_template.advent_of_code_utils import parse_args


class Task11Tests(TaskTest, unittest.TestCase):
    task = Task11(parse_args([]))
    known_input = ["...#......\n",
                   ".......#..\n",
                   "#.........\n",
                   "..........\n",
                   "......#...\n",
                   ".#........\n",
                   ".........#\n",
                   "..........\n",
                   ".......#..\n",
                   "#...#....."]
    known_output = 374
    known_bonus_output = 8410

    def test_given_bonus_example(self):
        assert solve_task_generic(self.known_input, 99) == self.known_bonus_output
