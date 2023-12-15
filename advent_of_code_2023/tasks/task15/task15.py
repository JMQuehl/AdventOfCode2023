from collections import deque

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Deque, Dict, Tuple
import re


def get_hash(text: str) -> int:
    """
    Calculates the hash value of the given string.
    """
    current_value = 0
    for char in text:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


def process_instruction(instruction: str, lense_map: Dict[int, Deque[Tuple[str, int]]]):
    """
    interprets and applies the instruction to the lense_map
    """
    label = ''.join([i for i in instruction if i.isalpha()])
    hash_value = get_hash(label)
    if instruction.endswith('-'):
        if hash_value in lense_map:
            new_lenses = deque()
            for lense in lense_map[hash_value]:
                if lense[0] != label:
                    new_lenses.append(lense)
            lense_map[hash_value] = new_lenses
    else:
        focal_length = int(re.findall('\d+', instruction)[0])
        if not hash_value in lense_map:
            lense_map[hash_value] = deque([(label, focal_length)])
        else:
            new_lenses = deque()
            found = False
            for lense in lense_map[hash_value]:
                if lense[0] != label:
                    new_lenses.append(lense)
                else:
                    new_lenses.append((label, focal_length))
                    found = True
            if not found:
                new_lenses.append((label, focal_length))
            lense_map[hash_value] = new_lenses


class Task15(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = '%d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 15

    def solve_task(self, input_file_content: List[str]):
        return sum([get_hash(x) for x in input_file_content[0].strip().split(',')])

    def solve_bonus_task(self, input_file_content: List[str]):
        instructions = input_file_content[0].strip().split(',')
        lense_map = {}
        for instruction in instructions:
            process_instruction(instruction, lense_map)
        sum_of_focal_power = 0
        for i in range(256):
            if i in lense_map:
                for j, lens in enumerate(lense_map[i]):
                    sum_of_focal_power += (1 + i) * (j + 1) * lens[1]
        return sum_of_focal_power

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("([a-z]+((=\d+)|-))(,[a-z]+((=\d+)|-))*\n?", line) for line in input_file_content)
