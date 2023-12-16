from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2023.tasks.task16.task16 import Task16
from advent_of_code_2023.advent_of_code_utils import parse_args


class Task16Tests(TaskTest, unittest.TestCase):
    task = Task16(parse_args([]))
    known_input = [r".|...\....",
                   r"|.-.\.....",
                   r".....|-...",
                   r"........|.",
                   r"..........",
                   r"........."'\\',
                   r"..../.\\..",
                   r".-.-/..|..",
                   r".|....-|."'\\',
                   r"..//.|...."]
    known_output = 46
    known_bonus_output = 51
