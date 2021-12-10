import math
from collections import defaultdict
from typing import Generator

from colorama import Fore, Style

MAX_HEIGHT = 9

INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def main(input_lines: list[str]) -> int:
    # we use 9+1, to omit these while printing
    coords = defaultdict(lambda: MAX_HEIGHT + 1)
    low_points: list[tuple[int, int]] = []

    for y, line in enumerate(input_lines):
        for x, val in enumerate(line):
            coords[(x, y)] = int(val)

    for (x, y), n in coords.items():
        if all(coords.get(neigh, MAX_HEIGHT) > n for neigh in get_neighbors(x, y)):
            low_points.append((x, y))

    basins: list[set[tuple[int, int]]] = []

    for x, y in low_points:
        basin: set[tuple[int, int]] = {(x, y)}
        basin = check_neighbors(coords, (x, y), basin)
        basins.append(basin)

    three_largest_basins = sorted(basins, reverse=True, key=len)[0:3]

    for basin in three_largest_basins:
        print_basin(coords, basin)
        print()

    three_largest_basin_size = [len(basin) for basin in three_largest_basins]
    print(f"{three_largest_basin_size=}")

    return math.prod(three_largest_basin_size)


def print_basin(
    coords: dict[tuple[int, int], int], basin: set[tuple[int, int]]
) -> None:
    y0 = 0
    for x, y in coords:
        if x >= 0 and y >= 0 and coords[(x, y)] < 10:
            if y > y0:  # go to the next line
                print(Style.RESET_ALL)
                y0 = y
            if (x, y) in basin:
                color = Fore.RED
            else:
                color = Fore.WHITE
            print(color + str(coords[(x, y)]), end="")
    print(Style.RESET_ALL)


def check_neighbors(
    coords: dict[tuple[int, int], int],
    point: tuple[int, int],
    basin: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    for x, y in get_neighbors(*point):
        if coords[(x, y)] < 9 and (x, y) not in basin:
            basin.add((x, y))
            basin = check_neighbors(coords, (x, y), basin)
    return basin


def get_neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def parse_input_file() -> list[str]:
    with open("day09/input.txt", "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 1134


def test_main_real_data():
    assert main(parse_input_file()) == 987840


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
