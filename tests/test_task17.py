from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task17.task17 import Task17
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task17Tests(TaskTest, unittest.TestCase):
    task = Task17(parse_args([]))
    known_input = ["2413432311323\n",
                   "3215453535623\n",
                   "3255245654254\n",
                   "3446585845452\n",
                   "4546657867536\n",
                   "1438598798454\n",
                   "4457876987766\n",
                   "3637877979653\n",
                   "4654967986887\n",
                   "4564679986453\n",
                   "1224686865563\n",
                   "2546548887735\n",
                   "4322674655533"]
    known_output = 102
    known_bonus_output = 94
