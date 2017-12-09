from typing import List

GLOBAL_MAX_VALUE: int = 10 ** 7
SQUARES: List[int] = [d * d for d in range(10)]


def get_digits_from_number(n: int) -> List[int]:
    return [int(c) for c in list(str(n))]


def is_christmas_number(n: int, max_value_of_any_number_in_sequence: int = GLOBAL_MAX_VALUE) -> bool:
    if n == 1:
        return True

    causes_infinite_loop: bool = n == 89 or n == 0

    if causes_infinite_loop:
        return False

    if n > max_value_of_any_number_in_sequence:
        return False

    sum_of_squared_digits: int = sum([SQUARES[d] for d in get_digits_from_number(n)])
    return is_christmas_number(sum_of_squared_digits)


if __name__ == '__main__':
    running_sum = 0

    for i in range(1, GLOBAL_MAX_VALUE + 1):
        if is_christmas_number(i):
            running_sum += i

    print(running_sum)
