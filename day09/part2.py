import math

from colorama import Fore, Style

INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def main(input_lines: list[str]) -> int:
    matrix = [[int(n) for n in line] for line in input_lines]
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


def print_basin(matrix: list[list[int]], basin: set[tuple[int, int]]) -> None:
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
    matrix: list[list[int]], point: tuple[int, int], basin: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    for neigh in get_neighbors(matrix, point):
        if matrix[neigh[0]][neigh[1]] < 9 and neigh not in basin:
            basin.add(neigh)
            basin = check_neighbors(matrix, neigh, basin)
    return basin


def get_neighbors(
    matrix: list[list[int]], point: tuple[int, int]
) -> list[tuple[int, int]]:
    row_i, col_i = point
    neighbors = []

    if row_i != 0:
        neighbors.append((row_i - 1, col_i))

    if row_i != len(matrix) - 1:
        neighbors.append((row_i + 1, col_i))

    if col_i != 0:
        neighbors.append((row_i, col_i - 1))

    if col_i != len(matrix[0]) - 1:
        neighbors.append((row_i, col_i + 1))

    return neighbors


def are_neighbors_bigger(
    matrix: list[list[int]], number: int, row_i: int, col_i: int
) -> bool:
    # top
    if row_i != 0 and number >= matrix[row_i - 1][col_i]:
        return False
    # bottom
    if row_i != len(matrix) - 1 and number >= matrix[row_i + 1][col_i]:
        return False
    # left
    if col_i != 0 and number >= matrix[row_i][col_i - 1]:
        return False
    # right
    if col_i != len(matrix[0]) - 1 and number >= matrix[row_i][col_i + 1]:
        return False

    return True


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
