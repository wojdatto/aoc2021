from collections import defaultdict
from pathlib import Path
from typing import Generator

import pytest

ITERATIONS = 50

INPUT = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##\
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###\
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.\
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....\
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..\
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....\
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def main(s: str) -> int:
    algorithm_s, image = parse_input_data(s)

    algorithm = defaultdict(int)
    for i, char in enumerate(algorithm_s):
        if char == "#":
            algorithm[i] = 1

    pixels = defaultdict(int)
    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            if pixel == "#":
                pixels[(x, y)] = 1

    invert = int(algorithm[0] == 1 and algorithm[511] == 0)

    x_min = min(x for x, _ in pixels)
    x_max = max(x for x, _ in pixels)
    y_min = min(y for _, y in pixels)
    y_max = max(y for _, y in pixels)

    for i in range(ITERATIONS // 2):
        pixels1 = defaultdict(
            lambda: invert,
            {
                (x, y): algorithm[get_binary_num(x, y, pixels)]
                for y in range(y_min - 1, y_max + 2)
                for x in range(x_min - 1, x_max + 2)
            },
        )
        pixels = defaultdict(
            int,
            {
                (x, y): algorithm[get_binary_num(x, y, pixels1)]
                for y in range(y_min - 2, y_max + 3)
                for x in range(x_min - 2, x_max + 3)
            },
        )
        x_min -= 2
        y_min -= 2
        x_max += 2
        y_max += 2

    return sum(pixels.values())


def get_binary_num(x: int, y: int, pixels: defaultdict[tuple[int, int], int]) -> int:
    num_s = ""
    for x_n, y_n in get_pixel_with_neighbors(x, y):
        num_s += str(pixels[x_n, y_n])
    return int(num_s, 2)


def get_pixel_with_neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def parse_input_data(s: str) -> tuple[str, list[str]]:
    algorithm, image_s = s.split("\n\n")
    image = image_s.splitlines()
    return algorithm, image


def parse_input_file() -> str:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read()


if __name__ == "__main__":
    test_result = main(INPUT)
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT) == 3351


@pytest.mark.slow
def test_main_real_data():
    assert main(parse_input_file()) == 17628
