import math
import re
from collections import deque

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task05(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The lowest location number that corresponds to any seed is: %d"
        self.bonus_answer_text = "With interval interpretation the lowest location number for any seed is: %d"
        self.task_number = 5

    def parse_input(self, input_file_content: List[str]):
        seeds = [int(x) for x in re.findall('\d+', input_file_content[0])]
        all_maps = []
        current_map = []
        for line in input_file_content[3:]:
            if re.fullmatch('\d+( \d+)*\n?', line):
                current_map.append([int(x) for x in re.findall('\d+', line)])
            elif re.fullmatch('[a-zA-Z]+-[a-zA-Z]+-[a-zA-Z]+ map:\n?', line):
                continue
            else:
                all_maps.append(current_map)
                current_map = []
        all_maps.append(current_map)
        return seeds, all_maps

    def solve_task(self, input_file_content: List[str]) -> int:
        min_distance = math.inf
        seeds, maps = self.parse_input(input_file_content)
        for seed in seeds:
            current_value = seed
            for seed_map in maps:
                for mapping in seed_map:
                    if mapping[1] <= current_value < mapping[1] + mapping[2]:
                        current_value = mapping[0] + current_value - mapping[1]
                        break
            min_distance = min(min_distance, current_value)
        return min_distance

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        seeds, maps = self.parse_input(input_file_content)
        range_pool = deque([(x[0], x[0] + x[1] - 1) for x in zip(seeds[::2], seeds[1::2])])
        next_range_pool = deque()
        for seed_map in maps:
            while len(range_pool) > 0:
                start, end = range_pool.popleft()
                remainder_left = True
                for mapping in seed_map:
                    if mapping[1] <= start < mapping[1] + mapping[2]:
                        if end < mapping[1] + mapping[2]:
                            # whole interval is contained
                            next_range_pool.append((mapping[0] + start - mapping[1], mapping[0] + end - mapping[1]))
                            remainder_left = False
                            break
                        else:
                            # split interval
                            next_range_pool.append((mapping[0] + start - mapping[1], mapping[0] + mapping[2] - 1))
                            start = mapping[1] + mapping[2]
                    elif mapping[1] <= end < mapping[1] + mapping[2]:
                        # split interval
                        next_range_pool.append((mapping[0], mapping[0] + end - mapping[1]))
                        end = mapping[1] - 1
                    elif start <= mapping[1] < end:
                        # mapping interval is in current interval
                        next_range_pool.append((mapping[0], mapping[0] + mapping[2] - 1))
                        range_pool.append((start, mapping[1] - 1))
                        start = mapping[1] + mapping[2]
                if remainder_left:
                    next_range_pool.append((start, end))
            range_pool = next_range_pool
            next_range_pool = deque()
        return min(x[0] for x in range_pool)


    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch(
            '(seeds: [\d ]+\n?|\n?|'
            'seed-to-soil map:\n?|\d+( \d+)*\n?|'
            'soil-to-fertilizer map:\n?|'
            'fertilizer-to-water map:\n|'
            'water-to-light map:\n?|'
            'light-to-temperature map:\n?|'
            'temperature-to-humidity map:\n?|'
            'humidity-to-location map:\n?)',
            line) or re.fullmatch('', line) for line in input_file_content)
