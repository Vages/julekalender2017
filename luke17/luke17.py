def last_digit(n: int) -> int:
    return int(str(n)[-1])


def move_last_digit_first(n: int) -> int:
    n_as_string: str = str(n)
    return int(n_as_string[-1:] + n_as_string[0:-1])


if __name__ == '__main__':
    i: int = 0

    while not (last_digit(i) == 6 and move_last_digit_first(i) == 4 * i):
        i += 1

    print(i)
