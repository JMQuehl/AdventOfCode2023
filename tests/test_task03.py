from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task03.task03 import Task03
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task03(parse_args([]))
    known_input = ["467..114..\n",
                   "...*......\n",
                   "..35..633.\n",
                   "......#...\n",
                   "617*......\n",
                   ".....+.58.\n",
                   "..592.....\n",
                   "......755.\n",
                   "...$.*....\n",
                   ".664.598.."]
    known_output = 4361
    known_bonus_output = 467835
