import re
from collections import defaultdict

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple


def reduce_problem(locations: str):
    return re.sub('[.]+', '.', locations).strip('.')


class Task12(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of possibilities for broken spring locations is: %d"
        self.bonus_answer_text = "After unfolding the sum of possibilities is now: %d"
        self.task_number = 12
        self.history_book = defaultdict(dict)

    def get_number_of_possibilities(self, locations: str, numbers: Tuple[int]) -> int:
        """
        Idea: Use recursion with memoization.
        """
        if not numbers:  # base case. This is only a valid solution if no remaining location has to contain a spring.
            return 1 if all(ch != '#' for ch in locations) else 0
        if len(locations) < sum(numbers):  # base case. No placement is possible
            return 0
        if locations.startswith('.'):  # remove leading working springs
            return self.get_number_of_possibilities(locations[1:], numbers)
        if locations in self.history_book and numbers in self.history_book[locations]:  # This was already solved.
            return self.history_book[locations][numbers]
        possibilities = 0
        if all(ch != '.' for ch in locations[:numbers[0]]) and (
                len(locations) == numbers[0] or locations[
            numbers[0]] != '#'):  # Add all versions starting the first number in the first location
            possibilities += self.get_number_of_possibilities(locations[numbers[0] + 1:], numbers[1:])
        if locations[0] == '?':  # Add all versions starting the first number at least one location later
            possibilities += self.get_number_of_possibilities(locations[1:], numbers)

        self.history_book[locations][
            numbers] = possibilities  # add the new result to the list of previously solved ones.
        return possibilities

    def solve_task(self, input_file_content: List[str]) -> int:
        total = 0
        for line in input_file_content:
            locations = line.split(' ')[0]
            numbers = tuple([int(x) for x in re.findall('\d+', line.split(' ')[1])])
            total += self.get_number_of_possibilities(reduce_problem(locations), numbers)
        return total

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        total = 0
        for line in input_file_content:
            locations = ((line.split(' ')[0] + '?') * 5)[:-1]
            numbers = tuple([int(x) for x in re.findall('\d+', line.split(' ')[1])] * 5)
            total += self.get_number_of_possibilities(reduce_problem(locations), numbers)
        return total

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('[?#.]+ \d+(,\d+)*\n?', line) for line in input_file_content)
