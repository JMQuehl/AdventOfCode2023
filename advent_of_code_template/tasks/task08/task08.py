import math
import re

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Dict, Tuple


def parse_input(input_file_content: List[str]) -> (List[int], Dict[str, Tuple[str, str]]):
    lr_list = [0 if x == 'L' else 1 for x in input_file_content[0].strip()]
    map_nodes = {}
    for node_str in input_file_content[2:]:
        instructions = list(re.findall('[0-9A-Z]+', node_str))
        map_nodes[instructions[0]] = (instructions[1], instructions[2])
    return lr_list, map_nodes


class Task08(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "You need %d steps to reach ZZZ"
        self.bonus_answer_text = "You need %d steps until all ghosts reach a node ending with Z."
        self.task_number = 8

    def solve_task(self, input_file_content: List[str]) -> int:
        lr_list, map_nodes = parse_input(input_file_content)
        steps = 0
        current_node = 'AAA'
        while current_node != 'ZZZ':
            current_node = map_nodes[current_node][lr_list[steps % len(lr_list)]]
            steps += 1
        return steps

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        """
        This solution assumes that each start only ever leads to one goal and that each ghost goes around in cycles.
        If both is the case, then the mathematical idea is simple: Each ghost walks around a circle with a fixed size.
        By calculating how far each one is away from its respective goal, we can find how many steps are needed until
        each ghost is at the correct offset from the start by getting the least common multiple.
        """
        lr_list, map_nodes = parse_input(input_file_content)
        steps = 0
        current_nodes = [x for x in map_nodes.keys() if x[-1] == 'A']
        nearest_z = [math.inf for x in current_nodes]
        while any([x == math.inf for x in nearest_z]):
            current_nodes = [map_nodes[x][lr_list[steps % len(lr_list)]] for x in current_nodes]
            steps += 1
            for i in range(len(current_nodes)):
                if current_nodes[i][-1] == 'Z' and nearest_z[i] == math.inf:
                    nearest_z[i] = steps
        return math.lcm(*nearest_z)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('([RL]+\n?)|\n?|([A-Z]{3} = \([A-Z]{3}, [A-Z]{3}\)\n?)', line) for line in input_file_content)
