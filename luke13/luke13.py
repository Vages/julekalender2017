from typing import List

from luke02.luke02 import int_has_odd_number_of_ones


def get_loot_values(loot_list: List[str]) -> List[int]:
    value_index = 1
    return [int(line.split(',')[value_index]) for line in loot_list]


def is_bobs_loot(n: int) -> bool:
    return int_has_odd_number_of_ones(n)


if __name__ == '__main__':
    loot = [line.strip() for line in open('./loot.txt', encoding='utf8')]
    loot_values = sorted(get_loot_values(loot), reverse=True)
    print(sum([value for i, value in enumerate(loot_values) if is_bobs_loot(i)]))
