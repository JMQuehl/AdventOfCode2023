from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task10.task10 import Task10
from advent_of_code_template.advent_of_code_utils import parse_args


class Task10Tests(TaskTest, unittest.TestCase):
    task = Task10(parse_args([]))
    known_input = ["-L|F7\n",
                   "7S-7|\n",
                   "L|7||\n",
                   "-L-J|\n",
                   "L|-JF"]
    known_bonus_input = [".F----7F7F7F7F-7....\n",
                         ".|F--7||||||||FJ....\n",
                         ".||.FJ||||||||L7....\n",
                         "FJL7L7LJLJ||LJ.L-7..\n",
                         "L--J.L7...LJS7F-7L7.\n",
                         "....F-J..F7FJ|L7L7L7\n",
                         "....L7.F7||L7|.L7L7|\n",
                         ".....|FJLJ|FJ|F7|.LJ\n",
                         "....FJL-7.||.||||...\n",
                         "....L---J.LJ.LJLJ..."]
    known_output = 4
    known_bonus_output = 8

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_bonus_input) == self.known_bonus_output
