import re
from functools import cmp_to_key

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List

card_values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11,
               'A': 12}
card_values2 = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11,
                'A': 12}

ranks = ([1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5])


def get_rank_value(hand: str) -> int:
    return ranks.index(sorted(hand.count(card) for card in set(hand)))


def get_alternative_rank_value(hand: str) -> int:
    joker_count = hand.count('J')
    bare_hand = hand.replace('J', '')
    rank = sorted(bare_hand.count(card) for card in set(bare_hand)) if not bare_hand == '' else [0]
    rank[-1] += joker_count
    return ranks.index(rank)


def compare(first: str, second: str, use_alternate_calculation: bool = False):
    if not use_alternate_calculation:
        first_rank = get_rank_value(first)
        second_rank = get_rank_value(second)
    else:
        first_rank = get_alternative_rank_value(first)
        second_rank = get_alternative_rank_value(second)
    if first_rank != second_rank:
        return first_rank - second_rank
    for i in range(len(first)):
        if first[i] != second[i]:
            if not use_alternate_calculation:
                return card_values[first[i]] - card_values[second[i]]
            else:
                return card_values2[first[i]] - card_values2[second[i]]


def solve_task_generic(input_file_content: List[str], alternate_joker_rule=False) -> int:
    hands = []
    for input in input_file_content:
        split_input = input.strip().split(' ')
        hands.append((split_input[0], int(split_input[1])))
    hands.sort(key=cmp_to_key(lambda x, y: compare(x[0], y[0], alternate_joker_rule)))
    result_sum = 0
    for i in range(len(hands)):
        result_sum += (i + 1) * hands[i][1]
    return result_sum


class Task07(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "My total winnings are: %d"
        self.bonus_answer_text = "My total winnings using the new set of rules are: %d"
        self.task_number = 7

    def solve_task(self, input_file_content: List[str]) -> int:
        return solve_task_generic(input_file_content)

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        return solve_task_generic(input_file_content, True)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('[2-9AKTJQ]+ \d+\n?', line) for line in input_file_content)
