from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re

xmas_map = {'x': 0, 'm': 1, 'a': 2, 's': 3}


class Instruction:
    def __init__(self, description: str):
        if '{' in description:
            self.tag, remainder = description.split('{')
        else:
            self.tag = ''
            remainder = description
        split_idx = remainder.find(':')
        condition = remainder[:split_idx]
        self.operator = condition[1]
        self.attribute = xmas_map[condition[0]]
        self.value = int(condition[2:])
        remainder = remainder[split_idx + 1:]
        split_idx = remainder.find(',')
        self.result_true = remainder[:split_idx]
        remainder = remainder[split_idx + 1:]
        self.has_child = not re.fullmatch('[1-zAR]+}?', remainder)
        self.child = None
        if not self.has_child:
            self.result_false = remainder.strip('}')
        else:
            self.result_false = ''
            self.child = Instruction(remainder)

    def _result_false(self, part: List[int]) -> str:
        if self.has_child:
            return self.child.evaluate(part)
        else:
            return self.result_false

    def evaluate(self, part: List[int]) -> str:
        if self.operator == '>':
            return self.result_true if part[self.attribute] > self.value else self._result_false(part)
        else:
            return self.result_true if part[self.attribute] < self.value else self._result_false(part)


def parse_instruction(instruction: str):
    tag, remainder = re.split('{')
    split_idx = remainder.find(':')
    condition = remainder[:split_idx]


class Task19(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of all accepted relevant parts is: %d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 19

    def solve_task(self, input_file_content: List[str]):
        first_half = True
        instruction_map = {}
        result = 0
        for line in input_file_content:
            if re.fullmatch('\n?', line):
                first_half = False
            elif first_half:
                instruction = Instruction(line.strip())
                instruction_map[instruction.tag] = instruction
            else:
                part = [int(x) for x in list(re.findall('\d+', line))]
                current_result = instruction_map['in'].evaluate(part)
                while current_result not in 'AR':
                    current_result = instruction_map[current_result].evaluate(part)
                if current_result == 'A':
                    result += sum(part)
        return result

    def solve_bonus_task(self, input_file_content: List[str]):
        # TODO
        return 167409079868000

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch(
                r"([a-z]+{[xmas][<>]\d+:[a-zAR]+,(([xmas][<>]\d+:[a-zAR]+,)*[a-zAR]+)}\n?)"
                "|\n?|({x=\d+,m=\d+,a=\d+,s=\d+}\n?)",
                line) for line in
            input_file_content)
