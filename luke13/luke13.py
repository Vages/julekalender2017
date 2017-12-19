from typing import List

from luke02.luke02 import int_has_odd_number_of_ones


def read_file_to_string_array(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf8') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def get_loot_values(loot_list: List[str]) -> List[int]:
    value_index = 1
    return [int(line.split(',')[value_index]) for line in loot_list]


def is_bobs_loot(n: int) -> bool:
    return int_has_odd_number_of_ones(n)


if __name__ == '__main__':
    loot = read_file_to_string_array('./loot.txt')
    loot_values = sorted(get_loot_values(loot), reverse=True)
    print(sum([value for i, value in enumerate(loot_values) if is_bobs_loot(i)]))
