from copy import copy
from pathlib import Path

INPUT = """\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""


def main(s: list[str]) -> int:
    points: dict[tuple[int, int], str] = {}
    for y, line in enumerate(s):
        for x, p in enumerate(line):
            points[(x, y)] = p

    max_x, max_y = max(points.keys())
    iteration = 0
    is_move = True
    while is_move:
        # print_points(points)
        is_move = False
        points_cp = copy(points)

        for (x, y), p in points_cp.items():
            if p == ">":
                x_n = x + 1 if x < max_x else 0
                if points_cp[(x_n, y)] == ".":
                    points[(x_n, y)] = ">"
                    points[(x, y)] = "."
                    is_move = True

        points_cp = copy(points)

        for (x, y), p in points_cp.items():
            if p == "v":
                y_n = y + 1 if y < max_y else 0
                if points_cp[(x, y_n)] == ".":
                    points[(x, y_n)] = "v"
                    points[(x, y)] = "."
                    is_move = True
        iteration += 1
    return iteration


def print_points(points: dict[tuple[int, int], str]):
    max_x, max_y = max(points.keys())
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(points[(x, y)], end="")
        print()
    print()


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT.splitlines()) == 58


def test_main_real_data():
    assert main(parse_input_file()) == 419
