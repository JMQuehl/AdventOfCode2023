from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task15.task15 import Task15, get_hash
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task15Tests(TaskTest, unittest.TestCase):
    task = Task15(parse_args([]))
    known_input = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]
    known_output = 1320
    known_bonus_output = 145

    def test_hash_function(self):
        assert get_hash('HASH') == 52
