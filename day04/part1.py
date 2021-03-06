from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

ROWS = 5
COLUMNS = 5
NUMBERS_IDX = 0
BOARDS_DATA_START = 2


class Game:
    def __init__(self, numbers: list[int], boards: list[Board]) -> None:
        self.numbers = numbers
        self.boards = boards

    def play_game(self):
        for number in self.numbers:
            for board in self.boards:
                board.truth_matrix = (board.matrix == number) | (board.truth_matrix)
                if self.check_if_won(board.truth_matrix):
                    sum_of_unmarked = sum(
                        board.matrix[np.where(board.truth_matrix == 0)]
                    )
                    final_result = number * sum_of_unmarked
                    return final_result

    def check_if_won(self, matrix: NDArray) -> bool:
        if (matrix == 1).all(axis=1).any():
            return True
        if (matrix == 1).all(axis=0).any():
            return True
        return False


@dataclass
class Board:
    numbers: list[int]
    matrix: NDArray = field(init=False)
    truth_matrix: NDArray = np.full((ROWS, COLUMNS), False, dtype=bool)

    def __post_init__(self):
        self.matrix = np.array(self.numbers).reshape(ROWS, COLUMNS)


INPUT = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def read_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def parse_file(data: list[str]) -> Game:
    numbers = get_numbers(data[NUMBERS_IDX])
    boards = construct_boards(data[BOARDS_DATA_START:])
    return Game(numbers, boards)


def get_numbers(row: str) -> list[int]:
    return [int(number) for number in row.split(",")]


def construct_boards(data: list[str]) -> list[Board]:
    board_numbers: list[int] = []
    boards: list[Board] = []
    for line in data:
        if line == "":
            boards.append(Board(board_numbers))
            board_numbers = []
        board_numbers += [int(number) for number in line.split()]
    return boards


def test_play_game_example_data():
    game = parse_file(INPUT.split("\n"))
    assert game.play_game() == 4512


def test_play_game_real_data():
    game = parse_file(read_file())
    assert game.play_game() == 12796


if __name__ == "__main__":
    test_game = parse_file(INPUT.split("\n"))
    test_result = test_game.play_game()
    print(f"{test_result=}")

    lines = read_file()
    real_game = parse_file(lines)
    real_result = real_game.play_game()
    print(f"{real_result=}")
