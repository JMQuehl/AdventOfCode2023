from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task09.task09 import Task09
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task09Tests(TaskTest, unittest.TestCase):
    task = Task09(parse_args([]))
    known_input = ["0 3 6 9 12 15\n",
                   "1 3 6 10 15 21\n",
                   "10 13 16 21 30 45"]
    known_output = 114
    known_bonus_output = 2
