from collections import defaultdict
from copy import copy
from pathlib import Path
from typing import Generator

OUT_OF_BOUNDARY = -1
GRID_SIZE = 10
STEPS = 100

INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def main(lines: list[str]) -> int:
    coords: defaultdict[tuple[int, int], int] = defaultdict(lambda: OUT_OF_BOUNDARY)
    for y, line in enumerate(lines):
        for x, level in enumerate(line):
            coords[(x, y)] = int(level)

    # print_coords(coords)

    flashes = 0
    for _ in range(STEPS):
        who_flashed = set()
        coords_cp = copy(coords)
        for x, y in coords_cp:
            coords, who_flashed = update_coords((x, y), coords, who_flashed)
        flashes += len(who_flashed)
        # print_coords(coords)

    return flashes


def update_coords(
    point: tuple[int, int],
    coords: defaultdict[tuple[int, int], int],
    who_flashed=set[tuple[int, int]],
) -> tuple[defaultdict[tuple[int, int], int], set[tuple[int, int]]]:

    x, y = point

    if coords[(x, y)] >= 0:  # to ignore points out of boundary
        if coords[(x, y)] == 9:
            who_flashed.add((x, y))
            coords[(x, y)] = 0

            for neigh in get_neighbors(x, y):
                coords, who_flashed = update_coords(neigh, coords, who_flashed)

        elif (x, y) not in who_flashed:
            coords[(x, y)] += 1

    return coords, who_flashed


def get_neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y - 1
    yield x - 1, y + 1


def print_coords(coords: defaultdict[tuple[int, int], int]):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            print(coords[(x, y)], end="")
        print()
    print("\n----------\n")


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 1656


def test_main_real_data():
    assert main(parse_input_file()) == 1649


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}\n")

    # print("\n==========\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")
