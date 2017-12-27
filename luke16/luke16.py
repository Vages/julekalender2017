from statistics import median
from typing import Set, List

prisoner_order: List[int] = [int(line.strip()) for line in open('./prisoners.txt')]


class LightBulb:
    def __init__(self):
        self._turned_on = False

    def flip_switch(self):
        self._turned_on = not self._turned_on

    def is_on(self):
        return self._turned_on


def lowest_number_of_visits_needed_before_quitting_with_given_order_and_given_leader(
        prisoner_order: List[int],
        leader_id: int) -> int:
    number_of_prisoners: int = len(set(prisoner_order))
    number_of_times_leader_has_seen_light_bulb_turned_on: int = 0

    prisoners_that_have_turned_the_light_on: Set[int] = set()
    light_bulb: LightBulb = LightBulb()

    for number_of_visits, visiting_prisoner in enumerate(prisoner_order, start=1):
        prisoner_is_the_leader: bool = visiting_prisoner == leader_id

        if prisoner_is_the_leader:
            if light_bulb.is_on():
                number_of_times_leader_has_seen_light_bulb_turned_on += 1
                leader_should_call_the_grinch: bool = \
                    number_of_times_leader_has_seen_light_bulb_turned_on == number_of_prisoners - 1

                if leader_should_call_the_grinch:
                    return number_of_visits

                light_bulb.flip_switch()
        else:
            if not light_bulb.is_on() and visiting_prisoner not in prisoners_that_have_turned_the_light_on:
                light_bulb.flip_switch()
                prisoners_that_have_turned_the_light_on.add(visiting_prisoner)


print(lowest_number_of_visits_needed_before_quitting_with_given_order_and_given_leader(prisoner_order, 1))
