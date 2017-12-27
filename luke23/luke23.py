from collections import defaultdict
from enum import Enum, auto
from typing import Set, FrozenSet, DefaultDict, List, Dict, Union

DRAWS_BEFORE_HUMANS_CHANGE_PLACES = 4


class Player(Enum):
    X = auto()
    O = auto()

    def __neg__(self):
        if self is self.X:
            return self.O
        return self.X


class Human(Enum):
    Xena = auto()
    Ophelia = auto()

    def __neg__(self):
        if self is self.Xena:
            return self.Ophelia
        return self.Xena


SEQUENCES_LEADING_TO_A_WIN_ON_A_BOARD: Set[FrozenSet[int]] = \
    set([
        frozenset(s) for s in

        [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},

         {1, 4, 7}, {2, 5, 8}, {3, 6, 9},

         {1, 5, 9}, {3, 5, 7}]
    ])

SEQUENCES_THAT_INVOLVE_A_GIVEN_CELL: DefaultDict[int, Set[FrozenSet[int]]] = defaultdict(set)

for sequence in SEQUENCES_LEADING_TO_A_WIN_ON_A_BOARD:
    for number in sequence:
        SEQUENCES_THAT_INVOLVE_A_GIVEN_CELL[number].add(sequence)


class TicTacToeGame:
    def __init__(self):
        self._player_moves_in_this_round: Dict[Player, Set[int]] = {Player.X: set(), Player.O: set()}
        self._current_player: Player = Player.X
        self._winning_player: Union[Player, None] = None

    def perform_move(self, move):
        if self.has_been_won_by_someone():
            raise ValueError("Someone has already won this game. No more moves allowed.")
        if move in self._player_moves_in_this_round[Player.X] | self._player_moves_in_this_round[Player.O]:
            raise ValueError("Cell %i has already been taken this round" % move)
        self._player_moves_in_this_round[self._current_player].add(move)

        for s in SEQUENCES_THAT_INVOLVE_A_GIVEN_CELL[move]:
            is_winning_sequence: bool = s.issubset(self._player_moves_in_this_round[self._current_player])
            if is_winning_sequence:
                self._winning_player = self._current_player

        self._current_player = -self._current_player

    def get_winning_player(self) -> Player:
        return self._winning_player

    def has_been_won_by_someone(self) -> bool:
        return self.get_winning_player() is not None

    def is_draw(self) -> bool:
        return len(self._player_moves_in_this_round[Player.X] | self._player_moves_in_this_round[
            Player.O]) == 9 and not self.has_been_won_by_someone()

    def __str__(self):
        the_string: str = ''

        for i in range(1, 10):
            if i in self._player_moves_in_this_round[Player.X]:
                the_string += "X "
            elif i in self._player_moves_in_this_round[Player.O]:
                the_string += "O "
            else:
                the_string += "_ "
            if not i % 3 and not i == 9:
                the_string += "\n"

        return the_string


if __name__ == '__main__':
    moves_from_all_games: List[int] = [int(i) for i in list(open('./moves.txt').readline())]

    victories: List[Union[Player, None]] = list()

    current_game: TicTacToeGame = TicTacToeGame()

    for move in moves_from_all_games:
        current_game.perform_move(move)

        game_resulted_in_a_win: bool = current_game.has_been_won_by_someone()
        game_resulted_in_a_draw: bool = current_game.is_draw()

        if game_resulted_in_a_win or game_resulted_in_a_draw:
            print(current_game)
            print(current_game.get_winning_player())
            print()

            if game_resulted_in_a_win:
                victories.append(current_game.get_winning_player())
            elif game_resulted_in_a_draw:
                victories.append(None)

            current_game = TicTacToeGame()

    human_who_plays_x: Human = Human.Xena
    victories_of_humans: DefaultDict[Human, int] = defaultdict(int)

    draws_in_a_row = 0

    for game_winner in victories:
        if game_winner is not None:
            if game_winner is Player.X:
                victories_of_humans[human_who_plays_x] += 1
            else:
                victories_of_humans[-human_who_plays_x] += 1

            draws_in_a_row = 0

        else:
            draws_in_a_row += 1

        if game_winner is Player.X or draws_in_a_row == DRAWS_BEFORE_HUMANS_CHANGE_PLACES:
            human_who_plays_x = -human_who_plays_x
            draws_in_a_row = 0

    print(victories_of_humans)
