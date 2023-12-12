from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task12.task12 import Task12
from advent_of_code_template.advent_of_code_utils import parse_args


class Task12Tests(TaskTest, unittest.TestCase):
    task = Task12(parse_args([]))
    known_input = ["???.### 1,1,3\n",
                   ".??..??...?##. 1,1,3\n",
                   "?#?#?#?#?#?#?#? 1,3,1,6\n",
                   "????.#...#... 4,1,1\n",
                   "????.######..#####. 1,6,5\n",
                   "?###???????? 3,2,1"]
    known_output = 21
    known_bonus_output = 525152
