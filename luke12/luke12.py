from enum import Enum, auto
from typing import List, Iterator

from luke02.luke02 import Coordinate, add

KNIGHT_MOVES = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]


class Color(Enum):
    WHITE = auto()
    BLACK = auto()

    def get_opposite(self):
        if self == self.BLACK:
            return self.WHITE
        return self.BLACK


class FlipBoard:
    def __init__(self, size):
        self._board: List[List[Color]] = [[Color.WHITE] * size for _ in range(size)]
        self._size: int = size
        self._current_cell: Coordinate = (0, 0)

    def _is_legal_position(self, coordinate: Coordinate) -> bool:
        return all(map(lambda x: 0 <= x < self._size, coordinate))

    def get_color(self, coordinate: Coordinate) -> Color:
        x, y = coordinate
        return self._board[y][x]

    def set_color(self, color: Color, coordinate: Coordinate) -> None:
        x, y = coordinate
        self._board[y][x] = color

    def get_cells_the_knight_can_move_to(self) -> Iterator[Coordinate]:
        return filter(self._is_legal_position, map(lambda x: add(self._current_cell, x), KNIGHT_MOVES))

    def get_next_move(self) -> Coordinate:
        cells_we_can_move_to: List[Coordinate] = list(self.get_cells_the_knight_can_move_to())

        legal_cells_with_same_color: List[Coordinate] = [
            cell for cell in cells_we_can_move_to if self.get_color(cell) == self.get_color(self._current_cell)]
        cells_with_same_color_exist = len(legal_cells_with_same_color) > 0
        if cells_with_same_color_exist:
            return min(legal_cells_with_same_color)
        return max(cells_we_can_move_to)

    def move(self, coordinate) -> None:
        self.reverse_cell(self._current_cell)
        self._current_cell = coordinate

    def move_to_best_cell(self) -> None:
        self.move(self.get_next_move())

    def get_number_of_black_cells(self) -> int:
        cumulative_sum: int = 0

        coordinates: List[Coordinate] = [(i, j) for i in range(self._size) for j in range(self._size)]

        for coordinate in coordinates:
            if self.get_color(coordinate) == Color.BLACK:
                cumulative_sum += 1

        return cumulative_sum

    def reverse_cell(self, coordinate) -> None:
        current_color: Color = self.get_color(coordinate)
        self.set_color(current_color.get_opposite(), coordinate)

    def __str__(self):
        BLACK_SYMBOL, WHITE_SYMBOL = '_', 'X'

        return \
            '\n'.join(
                [' '.join([BLACK_SYMBOL if cell == Color.BLACK else WHITE_SYMBOL for cell in row]) for row in
                 reversed(self._board)]
            )


if __name__ == '__main__':
    fb = FlipBoard(10)
    for i in range(200):
        fb.move_to_best_cell()
        print(fb)
        print(fb.get_number_of_black_cells())
        print()

    print(fb.get_number_of_black_cells())
