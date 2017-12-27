from heapq import heappush, heappop
from typing import Dict, List, Tuple, Set

from luke02.luke02 import Coordinate, add

DIRECTIONS: Dict[str, Coordinate] = {
    "O": (0, -1),
    "N": (0, 1),
    "V": (-1, 0),
    "H": (1, 0),
}


def read_string_to_coordinate(string: str) -> Coordinate:
    without_parentheses: str = string.strip()[1:-1]
    x, y = without_parentheses.split(',')
    return int(x), int(y)


class PortalGameBoard:
    def __init__(self, portals_file, board_size):
        self._board_size = board_size
        self._portals = self.construct_portal_dictionary(portals_file)

    @staticmethod
    def construct_portal_dictionary(file_path: str) -> Dict[Coordinate, Coordinate]:
        the_dictionary: Dict[Coordinate, Coordinate] = dict()

        for line in open(file_path):
            start, end = [read_string_to_coordinate(s) for s in line.strip().split('->')]
            the_dictionary[start] = end

        return the_dictionary

    def _is_legal_coordinate(self, c: Coordinate) -> bool:
        return all(map(lambda x: 0 <= x < self._board_size, c))

    def get_neighbors(self, c: Coordinate) -> Dict[str, Coordinate]:
        the_return_dict: Dict[str, Coordinate] = dict()
        for direction in DIRECTIONS:
            relative_coordinate: Coordinate = DIRECTIONS[direction]
            resulting_position: Coordinate = add(c, relative_coordinate)
            position_after_possibly_entering_portal: Coordinate = self._portals[
                resulting_position] if resulting_position in self._portals else resulting_position
            if self._is_legal_coordinate(position_after_possibly_entering_portal):
                the_return_dict[direction] = position_after_possibly_entering_portal

        return the_return_dict


if __name__ == '__main__':
    board_size = 10000
    game_board: PortalGameBoard = PortalGameBoard('./portals.txt', board_size)

    start_coordinate: Coordinate = (0, 0)
    end_coordinate: Coordinate = (board_size - 1, board_size - 1)

    best_predecessors_and_directions: Dict[Coordinate, Tuple[Coordinate, str]] = dict()

    priority_queue: List[Tuple[int, Coordinate, Coordinate, str]] = [(0, start_coordinate, None, None)]
    already_expanded: Set[Coordinate] = set()

    while priority_queue:
        cost_of_arrival, current_coordinate, predecessor, direction_of_arrival = heappop(priority_queue)

        if current_coordinate in already_expanded:
            continue

        already_expanded.add(current_coordinate)

        best_predecessors_and_directions[current_coordinate] = (predecessor, direction_of_arrival)

        if current_coordinate == end_coordinate:
            break

        neighbors = game_board.get_neighbors(current_coordinate)

        for direction in neighbors:
            next_coordinate = neighbors[direction]
            if next_coordinate not in already_expanded:
                heappush(priority_queue, (cost_of_arrival + 1, next_coordinate, current_coordinate, direction))

    next_coordinate_to_unravel: Coordinate = end_coordinate
    path_so_far = ''

    while next_coordinate_to_unravel is not None:
        next_coordinate_to_unravel, direction_of_arrival = best_predecessors_and_directions[next_coordinate_to_unravel]
        path_so_far += direction_of_arrival if direction_of_arrival is not None else ''

    print(len(path_so_far))
