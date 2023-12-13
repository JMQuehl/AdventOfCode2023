from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task01.task01 import Task01
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task01(parse_args([]))
    known_input = ["1abc2\n",
                   "pqr3stu8vwx\n",
                   "a1b2c3d4e5f\n",
                   "treb7uchet"]
    known_output = 142
    known_bonus_input = ["two1nine\n",
                         "eightwothree\n",
                         "abcone2threexyz\n",
                         "xtwone3four\n",
                         "4nineeightseven2\n",
                         "zoneight234\n",
                         "7pqrstsixteen"]
    known_bonus_output = 281

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_bonus_input) == self.known_bonus_output
