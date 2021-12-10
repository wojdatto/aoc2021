INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def main(input_lines: list[str]) -> int:
    matrix = [[int(n) for n in line] for line in input_lines]

    low_points: list[tuple[int, int, int]] = []

    for row_i, row in enumerate(matrix):
        for col_i, number in enumerate(row):
            if are_neighbors_bigger(matrix, number, row_i, col_i):
                low_points.append((row_i, col_i, number))

    return sum(number + 1 for _, _, number in low_points)


def are_neighbors_bigger(
    matrix: list[list[int]], number: int, row_i: int, col_i: int
) -> bool:
    # top
    if row_i != 0 and not number < matrix[row_i - 1][col_i]:
        return False
    # bottom
    if row_i != len(matrix) - 1 and not number < matrix[row_i + 1][col_i]:
        return False
    # left
    if col_i != 0 and not number < matrix[row_i][col_i - 1]:
        return False
    # right
    if col_i != len(matrix[0]) - 1 and not number < matrix[row_i][col_i + 1]:
        return False

    return True


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
