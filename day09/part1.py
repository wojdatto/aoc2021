import numpy as np
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

    low_points: list[tuple[int, int, int]] = []

    for row_i, row in enumerate(matrix):
        for col_i, number in enumerate(row):
            if are_neighbors_bigger(matrix, number, row_i, col_i):
                low_points.append((row_i, col_i, number))

    return sum(number + 1 for _, _, number in low_points)


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
    assert main(INPUT.splitlines()) == 15


def test_main_real_data():
    assert main(parse_input_file()) == 600


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
