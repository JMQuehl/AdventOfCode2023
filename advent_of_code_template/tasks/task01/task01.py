import re

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task01(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of all calibration values is: %d"
        self.bonus_answer_text = "The sum of all calibration values using spelt numbers as well is: %d"
        self.task_number = 1

    def solve_task(self, input_file_content: List[str]) -> int:
        digit_sum = 0
        for line in input_file_content:
            digits = re.findall('\d', line)  # search for all digits
            digit_sum += int(digits[0] + digits[-1])  # concat the first and last finding and add it to the sum
        return digit_sum

    list_of_literal_digits = [('one', '1'),
                              ('two', '2'),
                              ('three', '3'),
                              ('four', '4'),
                              ('five', '5'),
                              ('six', '6'),
                              ('seven', '7'),
                              ('eight', '8'),
                              ('nine', '9'),
                              ('1', '1'),
                              ('2', '2'),
                              ('3', '3'),
                              ('4', '4'),
                              ('5', '5'),
                              ('6', '6'),
                              ('7', '7'),
                              ('8', '8'),
                              ('9', '9')]

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        # note: this algorithm only works since there are no two numbers that contain each other in written form.
        # example: if 'eve' were a number, and a word would end with 'seven', then the value of 'eve' would be used
        # instead of 7.
        digit_sum = 0
        for line in input_file_content:
            findings: List[(int, int)] = []
            # search for each possible string in list_of_literal_digits
            for string, digit in self.list_of_literal_digits:
                matches = list(re.finditer(string, line))
                if matches:
                    # adds a tuple to findings which contains the start index and value of the match
                    findings.append((matches[0].start(), digit))
                    if len(matches) > 1:
                        findings.append((matches[-1].span()[0], digit))
            # Sorts by the beginning of each word. Since no spelling of any number contains another number,
            # this coincides with the order which you would get if you sorted by the end index of each match.
            findings.sort(key=lambda x: x[0])
            digit_sum += int(findings[0][1] + findings[-1][1])
        return digit_sum

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('\w*\d\w*\n?', line) for line in input_file_content)
