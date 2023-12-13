import re
from functools import reduce

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
from collections import defaultdict
from operator import mul


class Task03(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of all numbers in the engine schematic is: %d"
        self.bonus_answer_text = "The sum of all gear ratios in the engine is: %d"
        self.task_number = 3

    def solve_task(self, input_file_content: List[str]):
        sum = 0
        for i in range(len(input_file_content)):
            # idea: for every number in every line check around each number if there are special characters.
            # if yes, add the value to the sum
            line = input_file_content[i].strip()
            numbers_in_line = list(re.finditer('\d+', line))
            for match in numbers_in_line:
                matched = False
                start = max(0, match.span()[0] - 1)  # start index, where to search for the characters
                end = min(len(line), match.span()[1] + 1)  # end index, where to search for the characters
                if i > 0:  # check previous line
                    matched = matched or re.findall('(?!\.)[\W]', input_file_content[i - 1].strip()[start:end])
                if i + 1 < len(input_file_content):  # check next line
                    matched = matched or re.findall('(?!\.)[\W]', input_file_content[i + 1].strip()[start:end])
                if (match.span()[0] > 0 and line[start] != '.') or (
                        match.span()[1] < len(line) and line[end - 1] != '.'):  # check symbols before and after
                    matched = True
                if matched:
                    sum += int(match[0])
        return sum

    def solve_bonus_task(self, input_file_content: List[str]):
        gear_candidates = defaultdict(list)

        for i in range(len(input_file_content)):
            # idea: check for every number if a * symbol is around them. If yes, add the number to a dict which keeps
            # track which numbers are around a * at a given coordinate. In the end build the result of all dict entries
            # which contain exactly 2 numbers.
            line = input_file_content[i].strip()
            numbers_in_line = list(re.finditer('\d+', line))
            for match in numbers_in_line:
                start = max(0, match.span()[0] - 1)
                end = min(len(line), match.span()[1] + 1)
                if i > 0:
                    indices = [i for i, itr in enumerate(input_file_content[i - 1].strip()[start:end]) if itr == '*']
                    for index in indices:
                        gear_candidates[(i - 1, start + index)].append(int(match[0]))
                if i + 1 < len(input_file_content):
                    indices = [i for i, itr in enumerate(input_file_content[i + 1].strip()[start:end]) if itr == '*']
                    for index in indices:
                        gear_candidates[(i + 1, start + index)].append(int(match[0]))
                if match.span()[0] > 0 and line[start] == '*':
                    gear_candidates[(i, start)].append(int(match[0]))
                if match.span()[1] < len(line) and line[end - 1] == '*':
                    gear_candidates[(i, end - 1)].append(int(match[0]))

        return sum([reduce(mul, x) for x in gear_candidates.values() if len(x) == 2])

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('[\d\W]+\n?', line) for line in
                   input_file_content)
