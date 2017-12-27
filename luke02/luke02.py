import typing
from collections import Counter, deque

LabyrinthStructure = typing.List[typing.List[bool]]
Coordinate = typing.Tuple[int, int]
CoordinateList = typing.List[Coordinate]
CoordinateSet = typing.Set[Coordinate]

DIRECTIONS: typing.Tuple[Coordinate, Coordinate, Coordinate, Coordinate] = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Labyrinth:
    def __init__(self, size):
        self._structure: LabyrinthStructure = self.make_labyrinth_structure(size)
        self.size = size

    @staticmethod
    def make_labyrinth_structure(size: int) -> LabyrinthStructure:
        the_board = []

        for y in range(1, size + 1):
            current_row = []
            for x in range(1, size + 1):
                current_number = the_mysterious_function(x, y)
                current_row.append(int_has_odd_number_of_ones(current_number))

            the_board.append(current_row)

        return the_board

    def has_wall_at_cell(self, c: Coordinate) -> bool:
        x, y = c
        return self._structure[y][x]

    def get_neighbors(self, c: Coordinate) -> CoordinateList:
        candidates: CoordinateList = [add(c, d) for d in DIRECTIONS]
        return list(filter(self._is_legal_position, candidates))

    def get_open_neighbors(self, c: Coordinate) -> CoordinateList:
        ns: CoordinateList = self.get_neighbors(c)
        return list(filter(lambda x: not self.has_wall_at_cell(x), ns))

    def _is_legal_position(self, c: Coordinate) -> bool:
        for a in c:
            if not 0 <= a < self.size:
                return False

        return True

    def __str__(self):
        return '\n'.join([' '.join(["#" if cell else '_' for cell in row]) for row in self._structure])

    def get_open_cells(self) -> CoordinateSet:
        open_cells: CoordinateSet = set()

        for y in range(self.size):
            for x in range(self.size):
                if not self.has_wall_at_cell((x, y)):
                    open_cells.add((x, y))

        return open_cells


def the_mysterious_function(x: int, y: int) -> int:
    return x ** 3 + 12 * x * y + 5 * x * y ** 2


def has_odd_number_of_ones(binary_number: str) -> bool:
    count: typing.Counter = Counter(binary_number)
    return count['1'] % 2


def int_has_odd_number_of_ones(some_int: int) -> bool:
    int_as_binary: str = int_to_binary(some_int)
    return has_odd_number_of_ones(int_as_binary)


def int_to_binary(some_integer: int) -> str:
    return "{0:b}".format(some_integer)


def add(c1: Coordinate, c2: Coordinate) -> Coordinate:
    return c1[0] + c2[0], c1[1] + c2[1]


if __name__ == '__main__':
    the_labyrinth = Labyrinth(1000)

    places_to_visit: typing.Deque[Coordinate] = deque([(0, 1)])
    already_visited: CoordinateSet = set()

    while places_to_visit:
        now_visiting: Coordinate = places_to_visit.popleft()
        if now_visiting in already_visited:
            continue
        already_visited.add(now_visiting)
        open_neighbors: CoordinateList = the_labyrinth.get_open_neighbors(now_visiting)
        for n in open_neighbors:
            if n not in already_visited:
                places_to_visit.append(n)

    unreachable_cells: CoordinateSet = the_labyrinth.get_open_cells() - already_visited
    print(len(unreachable_cells))
