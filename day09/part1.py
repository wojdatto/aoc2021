from pathlib import Path
from typing import Generator

MAX_HEIGHT = 9

INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def main(input_lines: list[str]) -> int:
    coords = {}

    for y, line in enumerate(input_lines):
        for x, val in enumerate(line):
            coords[(x, y)] = int(val)

    low_points = 0

    for (x, y), n in coords.items():
        if all(coords.get(neigh, MAX_HEIGHT) > n for neigh in get_neighbors(x, y)):
            low_points += n + 1
    return low_points


def get_neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
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
