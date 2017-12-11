from typing import Set


def get_guests(max_guests: int) -> Set[int]:
    return {i for i in range(0, max_guests)}


def find_id_of_last_sitting_guest(initial_number_of_guests: int) -> int:
    seated_guests = get_guests(initial_number_of_guests)

    the_guest_with_the_bottle = 0

    def find_next_seated_guest() -> int:
        for i in range(1, initial_number_of_guests + 1):
            guest_who_we_wonder_whether_is_still_seated = (the_guest_with_the_bottle + i) % initial_number_of_guests
            if guest_who_we_wonder_whether_is_still_seated in seated_guests:
                return guest_who_we_wonder_whether_is_still_seated

    while len(seated_guests) > 1:
        seated_guests.remove(find_next_seated_guest())
        the_guest_with_the_bottle = find_next_seated_guest()

    return the_guest_with_the_bottle + 1


if __name__ == "__main__":
    print(find_id_of_last_sitting_guest(1500))
