from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task00.task00 import Task00
from advent_of_code_template.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task00(parse_args([]))
    known_input = ["\n"]
    known_output = -1
    known_bonus_output = -1
