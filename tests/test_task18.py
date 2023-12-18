from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task18.task18 import Task18
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task18Tests(TaskTest, unittest.TestCase):
    task = Task18(parse_args([]))
    known_input = ["R 6 (#70c710)\n",
                   "D 5 (#0dc571)\n",
                   "L 2 (#5713f0)\n",
                   "D 2 (#d2c081)\n",
                   "R 2 (#59c680)\n",
                   "D 2 (#411b91)\n",
                   "L 5 (#8ceee2)\n",
                   "U 2 (#caa173)\n",
                   "L 1 (#1b58a2)\n",
                   "U 2 (#caa171)\n",
                   "R 2 (#7807d2)\n",
                   "U 3 (#a77fa3)\n",
                   "L 2 (#015232)\n",
                   "U 2 (#7a21e3)"]
    known_output = 62
    known_bonus_output = 952408144115
