from typing import List


def number_of_ways_to_reach_step(n: int) -> int:
    start_value_for_step_0: int = 1
    ways_to_arrive_at_step: List[int] = [0] * (n + 1)
    ways_to_arrive_at_step[0] = start_value_for_step_0

    for step in range(1, n + 1):
        for steps_back in range(1, 4):
            the_step_we_could_have_arrived_from: int = step - steps_back
            if the_step_we_could_have_arrived_from < 0:
                continue
            ways_to_arrive_at_step[step] += ways_to_arrive_at_step[the_step_we_could_have_arrived_from]

    return ways_to_arrive_at_step[-1]


if __name__ == '__main__':
    print(number_of_ways_to_reach_step(30))
