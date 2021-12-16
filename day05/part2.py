from collections import Counter
from pathlib import Path

INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def main(lines: list[str], is_test: bool = False) -> int:
    coords: Counter[tuple[int, int]] = Counter()
    max_x, max_y = -1, -1

    for line in lines:
        start, end = line.split(" -> ")
        x1_s, y1_s = start.split(",")
        x2_s, y2_s = end.split(",")
        x1, y1, x2, y2 = int(x1_s), int(y1_s), int(x2_s), int(y2_s)

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        if x1 < x2:
            x_d = 1
        elif x1 > x2:  # to handle the situation when X coord in decreasing
            x_d = -1
        else:
            x_d = 0

        if y1 < y2:
            y_d = 1
        elif y1 > y2:  # to handle the situation when Y coord in decreasing
            y_d = -1
        else:
            y_d = 0

        x, y = x1, y1
        while (x, y) != (x2 + x_d, y2 + y_d):
            coords[(x, y)] += 1
            x += x_d
            y += y_d

    if is_test:
        print_all(coords, max_x, max_y)

    count = 0
    for _, val in coords.most_common():
        if val > 1:
            count += 1
        else:
            break

    return count


def print_all(coords: Counter[tuple[int, int]], max_x, max_y) -> None:
    for y in range(max_x + 1):
        for x in range(max_y + 1):
            if coords[(x, y)]:
                print(coords[(x, y)], end="")
            else:
                print(".", end="")
        print()


def parse_input() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


def test_play_game_example_data():
    assert main(INPUT.splitlines()) == 12


def test_play_game_real_data():
    assert main(parse_input()) == 18674


if __name__ == "__main__":
    test_result = main(INPUT.splitlines(), is_test=True)
    print(f"\n{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
