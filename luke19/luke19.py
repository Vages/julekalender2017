from functools import reduce
from typing import List, Dict, Tuple, Set

from luke02.luke02 import Coordinate, add
from luke13.luke13 import read_file_to_string_array

directions: Dict[str, Coordinate] = {
    'north': (0, 1),
    'east': (1, 0),
    'south': (0, -1),
    'west': (-1, 0),
}


def convert_line_to_instruction(line: str) -> Tuple[int, str]:
    steps, direction = line.split(', ')
    return int(steps), direction


class SnowyField:
    def __init__(self):
        self._current_position: Coordinate = (None, None)
        self._our_walk: List[Coordinate] = []
        self._move_to((0, 0))

    def _move_to(self, coordinate: Coordinate) -> None:
        self._current_position = coordinate
        self._our_walk.append(coordinate)

    def take_one_step_in_direction(self, direction: str):
        self._move_to(add(self._current_position, directions[direction]))

    def __str__(self):
        touched_char, untouched_char = "XX", "__"

        minimum_x_value, maximum_x_value, minimum_y_value, maximum_y_value = \
            reduce(
                lambda so_far, coordinate: (
                    min(so_far[0], coordinate[0]),
                    max(so_far[1], coordinate[0]),
                    min(so_far[2], coordinate[1]),
                    max(so_far[3], coordinate[1])),
                self._our_walk, (0, 0, 0, 0))
        dimensions = (maximum_x_value - minimum_x_value, maximum_y_value - minimum_y_value)

        width, height = dimensions

        touched_cells: Set[Coordinate] = set(self._our_walk)

        grid: List[List[str]] = []

        for row in range(height+1):
            row_values = []
            for column in range(width+1):
                absolute_coordinate: Coordinate = add((column, row), (minimum_x_value, minimum_y_value))
                if absolute_coordinate in touched_cells:
                    row_values.append(touched_char)
                else:
                    row_values.append(untouched_char)

            grid.append(row_values)

        return "\n".join([''.join(row) for row in reversed(grid)])


if __name__ == '__main__':
    untouched_field: SnowyField = SnowyField()

    instructions: List[Tuple[int, str]] = map(convert_line_to_instruction, read_file_to_string_array('./path.txt'))
    for steps, direction in instructions:
        for i in range(steps):
            untouched_field.take_one_step_in_direction(direction)

    print(untouched_field)
