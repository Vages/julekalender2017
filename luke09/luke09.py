def sum_of_integer_sequence_from_a_to_and_including_b(a: int, b: int) -> int:
    length_of_sequence: int = (b + 1) - a

    return ((a + b) * length_of_sequence) // 2


def calculate_total_budget(min_id: int, max_id: int, min_sequence_length: int = 2):
    total_budget: int = 0

    for sequence_length in range(min_sequence_length, max_id + 1):
        budget_for_this_sequence_length: int = 0

        max_start_number: int = max_id - (sequence_length - 1)
        for start_number in range(min_id, max_start_number + 1):
            end_number: int = start_number + sequence_length - 1

            sum_starting_at_this_start_number: int = sum_of_integer_sequence_from_a_to_and_including_b(start_number,
                                                                                                       end_number)
            this_and_no_more_sequences_of_this_length_will_matter_to_the_budget = \
                sum_starting_at_this_start_number > max_id

            if this_and_no_more_sequences_of_this_length_will_matter_to_the_budget:
                break
            else:
                budget_for_this_sequence_length += 1

        if budget_for_this_sequence_length == 0:
            break
        else:
            total_budget += budget_for_this_sequence_length

    return total_budget


if __name__ == '__main__':
    print(calculate_total_budget(1, 130000))

