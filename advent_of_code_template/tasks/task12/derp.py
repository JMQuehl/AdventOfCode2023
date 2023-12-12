import re
import functools as ft

def possible_placements(condition, spring):
    for m in re.finditer(rf'(?=([^\.]{{{spring}}}[^#]))', condition):
        i = m.span(1)[0]
        if '#' in condition[:i]:
            break
        yield condition[i + spring + 1:]

@ft.cache
def count_placements(condition, springs):
    if not springs:
        return '#' not in condition
    first_spring, rest_springs = springs[0], springs[1:]
    return sum(count_placements(rest_condition, rest_springs)
               for rest_condition
               in possible_placements(condition, first_spring))

def day12p2():
    with open("input.txt") as f:
        lines = [(f'.{"?".join([condition] * 5)}.',
                  tuple(map(int, springs.split(','))) * 5)
                 for condition, springs
                 in (line.strip().split() for line in f)]
    res = sum(count_placements(condition, springs) for condition, springs in lines)
    print(res)