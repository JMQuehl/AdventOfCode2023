from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task07.task07 import Task07
from advent_of_code_template.advent_of_code_utils import parse_args


class Task07Tests(TaskTest, unittest.TestCase):
    task = Task07(parse_args([]))
    known_input = ["32T3K 765\n",
                   "T55J5 684\n",
                   "KK677 28\n",
                   "KTJJT 220\n",
                   "QQQJA 483"]
    known_output = 6440
    known_bonus_output = 5905
