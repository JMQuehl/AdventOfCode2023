from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task05.task05 import Task05
from advent_of_code_template.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task05(parse_args([]))
    known_input = ["seeds: 79 14 55 13\n",
                   "\n",
                   "seed-to-soil map:\n",
                   "50 98 2\n",
                   "52 50 48\n",
                   "\n",
                   "soil-to-fertilizer map:\n",
                   "0 15 37\n",
                   "37 52 2\n",
                   "39 0 15\n",
                   "\n",
                   "fertilizer-to-water map:\n",
                   "49 53 8\n",
                   "0 11 42\n",
                   "42 0 7\n",
                   "57 7 4\n",
                   "\n",
                   "water-to-light map:\n",
                   "88 18 7\n",
                   "18 25 70\n",
                   "\n",
                   "light-to-temperature map:\n",
                   "45 77 23\n",
                   "81 45 19\n",
                   "68 64 13\n",
                   "\n",
                   "temperature-to-humidity map:\n",
                   "0 69 1\n",
                   "1 0 69\n",
                   "\n",
                   "humidity-to-location map:\n",
                   "60 56 37\n",
                   "56 93 4"]
    known_output = 35
    known_bonus_output = 46
