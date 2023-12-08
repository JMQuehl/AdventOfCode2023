from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task08.task08 import Task08
from advent_of_code_template.advent_of_code_utils import parse_args


class Task08Tests(TaskTest, unittest.TestCase):
    task = Task08(parse_args([]))
    known_input = ["RL\n",
                   "\n",
                   "AAA = (BBB, CCC)\n",
                   "BBB = (DDD, EEE)\n",
                   "CCC = (ZZZ, GGG)\n",
                   "DDD = (DDD, DDD)\n",
                   "EEE = (EEE, EEE)\n",
                   "GGG = (GGG, GGG)\n",
                   "ZZZ = (ZZZ, ZZZ)"]
    known_input2 = ["LLR\n",
                    "\n",
                    "AAA = (BBB, BBB)\n",
                    "BBB = (AAA, ZZZ)\n",
                    "ZZZ = (ZZZ, ZZZ)"]
    known_bonus_input = ["LR\n",
                         "\n",
                         "11A = (11B, XXX)\n",
                         "11B = (XXX, 11Z)\n",
                         "11Z = (11B, XXX)\n",
                         "22A = (22B, XXX)\n",
                         "22B = (22C, 22C)\n",
                         "22C = (22Z, 22Z)\n",
                         "22Z = (22B, 22B)\n",
                         "XXX = (XXX, XXX)"]

    known_output = 2
    known_output2 = 6
    known_bonus_output = 6

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == self.known_output and self.task.solve_task(
            self.known_input2) == self.known_output2

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_bonus_input) == self.known_bonus_output
