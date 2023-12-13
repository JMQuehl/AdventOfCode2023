from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task06.task06 import Task06
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task06Tests(TaskTest, unittest.TestCase):
    task = Task06(parse_args([]))
    known_input = ["Time:      7  15   30\n",
                   "Distance:  9  40  200"]
    known_output = 288
    known_bonus_output = 71503
