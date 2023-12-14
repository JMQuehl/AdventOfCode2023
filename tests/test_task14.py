from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task14.task14 import Task14
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task14Tests(TaskTest, unittest.TestCase):
    task = Task14(parse_args([]))
    known_input = ["O....#....\n",
                   "O.OO#....#\n",
                   ".....##...\n",
                   "OO.#O....O\n",
                   ".O.....O#.\n",
                   "O.#..O.#.#\n",
                   "..O..#O..O\n",
                   ".......O..\n",
                   "#....###..\n",
                   "#OO..#...."]
    known_output = 136
    known_bonus_output = 64
