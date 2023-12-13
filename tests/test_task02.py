from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task02.task02 import Task02
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task02(parse_args([]))
    known_input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
                   "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
                   "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
                   "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
                   "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
    known_output = 8
    known_bonus_output = 2286
