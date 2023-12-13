import re

from advent_of_code_2023.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
from collections import deque


class Task04(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "All scratch cards together are worth: %d"
        self.bonus_answer_text = "Ultimately you will have %d scratch cards."
        self.task_number = 4


    def parse_cards(self, input_file_content: List[str]) -> List[int]:
        """
        Parses the task input. The ith element of the result list will contain the number of winning numbers for
        the card with number i+1
        :param input_file_content: List containing each line of the task input
        :return: A list containing the winning numbers
        """
        return_list = []
        for line in input_file_content:
            parts = line.split(':')[1].split('|')
            winning_numbers = set(re.findall('\d+', parts[0]))
            your_numbers = re.findall('\d+', parts[1])
            winning_counter = 0
            for number in your_numbers:
                if number in winning_numbers:
                    winning_counter += 1
            return_list.append(winning_counter)
        return return_list

    def solve_task(self, input_file_content: List[str]):
        total_sum = 0
        card_list = self.parse_cards(input_file_content)
        for elem in card_list:
            total_sum += 2 ** (elem - 1) if elem > 0 else 0
        return total_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        # idea: instead of simulating the game, you just have to look at each card once and determine, how many cards
        # would be the result if only all cards from that point onwards existed. So by iterating backwards, you can
        # build a list which contains that value. The final result will be the sum of that list.
        card_values = self.parse_cards(input_file_content)
        spawn_table = [0] * len(card_values)
        for i in reversed(range(len(spawn_table))):
            number_of_spawns = card_values[i]
            spawn_table[i] = 1
            for j in range(min(number_of_spawns, len(spawn_table) - i - 1)):
                spawn_table[i] += spawn_table[i+j+1]
        return sum(spawn_table)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('Card +\d+: +(\d+ +)+\| +(\d+ *)+\n?', line) for line in
                   input_file_content)
