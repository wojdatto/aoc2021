from __future__ import annotations

from dataclasses import dataclass, field

ROWS = 5
COLUMNS = 5
NUMBERS_IDX = 0
BOARDS_DATA_START = 2

@dataclass
class Game:
    numbers: list[int]
    boards: list[Board]


@dataclass
class Board:
    numbers: list[int]


INPUT = """
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


def read_file(filename) -> list[str]:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def parse_file(data: list[str]) -> Game:
    numbers = get_numbers(data[NUMBERS_IDX])
    boards = construct_boards(data[BOARDS_DATA_START:])
    return Game(numbers, boards)


def get_numbers(row: str) -> list[int]:
    return [int(number) for number in row.split(",")]


def construct_boards(data: list[str]) -> list[Board]:
    for line in data:
        ...


if __name__ == "__main__":
    parse_file(INPUT.split("\n")[1:])
