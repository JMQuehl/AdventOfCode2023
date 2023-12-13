from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task13.task13 import Task13
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task13Tests(TaskTest, unittest.TestCase):
    task = Task13(parse_args([]))
    known_input = ["#.##..##.\n",
                   "..#.##.#.\n",
                   "##......#\n",
                   "##......#\n",
                   "..#.##.#.\n",
                   "..##..##.\n",
                   "#.#.##.#.\n",
                   "\n",
                   "#...##..#\n",
                   "#....#..#\n",
                   "..##..###\n",
                   "#####.##.\n",
                   "#####.##.\n",
                   "..##..###\n",
                   "#....#..#"]
    known_output = 405
    known_bonus_output = 400
