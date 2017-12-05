import typing


def golombs_sequence(n: int = 1) -> typing.List[int]:
    the_array: typing.List[int] = [0]

    for i in range(1, n + 1):
        if len(the_array) == i:
            number_to_append = times_to_append_it = the_array[-1] + 1
        else:
            number_to_append: int = i
            times_to_append_it: int = the_array[i]

        the_array += [number_to_append] * times_to_append_it

        if len(the_array) >= n + 1:
            break

    return the_array[1: n + 1]


if __name__ == "__main__":
    print(sum(golombs_sequence(10 ** 6)))
