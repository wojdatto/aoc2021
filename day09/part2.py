import math

import numpy as np
from colorama import Fore, Style
from numpy.typing import NDArray

INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def main(input_lines: list[str]) -> int:
    matrix = np.array([[int(n) for n in line] for line in input_lines])
    low_points: list[tuple[int, int]] = []

    for row_i, row in enumerate(matrix):
        for col_i, number in enumerate(row):
            if are_neighbors_bigger(matrix, number, row_i, col_i):
                low_points.append((row_i, col_i))

    basins: list[set[tuple[int, int]]] = []

    for point in low_points:
        basin: set[tuple[int, int]] = {point}
        basin = check_neighbors(matrix, point, basin)
        basins.append(basin)

    three_largest_basins = sorted(basins, reverse=True, key=len)[0:3]

    for basin in three_largest_basins:
        print_basin(matrix, basin)
        print()

    three_largest_basin_size = [len(basin) for basin in three_largest_basins]
    print(f"{three_largest_basin_size=}")

    return math.prod(three_largest_basin_size)


def print_basin(matrix: NDArray, basin: set[tuple[int, int]]) -> None:
    for ri, row in enumerate(matrix):
        for ci, number in enumerate(row):
            is_print = False
            for basin_row, basin_col in basin:
                if ri == basin_row and ci == basin_col:
                    is_print = True
                    break
            if is_print:
                print(Fore.RED + str(number), end="")
            else:
                print(Fore.WHITE + str(number), end="")
        print(Style.RESET_ALL)


def check_neighbors(
    matrix: NDArray, point: tuple[int, int], basin: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    row_i, col_i = point
    value = matrix[row_i, col_i]
    diff_matrix = matrix - value

    max_row_i = matrix.shape[0] - 1
    max_col_i = matrix.shape[1] - 1

    if row_i == 0:
        top = None
    else:
        top = row_i - 1, col_i

    if row_i == max_row_i:
        bottom = None
    else:
        bottom = row_i + 1, col_i

    if col_i == 0:
        left = None
    else:
        left = row_i, col_i - 1

    if col_i == max_col_i:
        right = None
    else:
        right = row_i, col_i + 1

    neighbors = [neigh for neigh in [right, left, top, bottom] if neigh]

    for neigh in neighbors:
        if diff_matrix[neigh] > 0 and matrix[neigh] < 9 and neigh not in basin:
            basin.add(neigh)
            basin = check_neighbors(matrix, neigh, basin)

    return basin


def are_neighbors_bigger(matrix: NDArray, number: int, row_i: int, col_i: int) -> bool:
    max_row_i = matrix.shape[0] - 1
    max_col_i = matrix.shape[1] - 1

    # Matrix corners
    if row_i == 0 and col_i == 0:
        return number < matrix[row_i, col_i + 1] and number < matrix[row_i + 1, col_i]
    if row_i == 0 and col_i == max_col_i:
        return number < matrix[row_i, col_i - 1] and number < matrix[row_i + 1, col_i]
    if row_i == max_row_i and col_i == 0:
        return number < matrix[row_i, col_i + 1] and number < matrix[row_i - 1, col_i]
    if row_i == max_row_i and col_i == max_col_i:
        return number < matrix[row_i, col_i - 1] and number < matrix[row_i - 1, col_i]

    # top row
    if row_i == 0:
        return (
            number < matrix[row_i, col_i - 1]
            and number < matrix[row_i, col_i + 1]
            and number < matrix[row_i + 1, col_i]
        )

    # bottom row
    if row_i == max_row_i:
        return (
            number < matrix[row_i, col_i - 1]
            and number < matrix[row_i, col_i + 1]
            and number < matrix[row_i - 1, col_i]
        )

    # first column
    if col_i == 0:
        return (
            number < matrix[row_i - 1, col_i]
            and number < matrix[row_i + 1, col_i]
            and number < matrix[row_i, col_i + 1]
        )

    # last column
    if col_i == max_col_i:
        return (
            number < matrix[row_i - 1, col_i]
            and number < matrix[row_i + 1, col_i]
            and number < matrix[row_i, col_i - 1]
        )

    # the rest
    return (
        number < matrix[row_i - 1, col_i]
        and number < matrix[row_i + 1, col_i]
        and number < matrix[row_i, col_i - 1]
        and number < matrix[row_i, col_i + 1]
    )


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
