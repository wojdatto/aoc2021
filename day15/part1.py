from collections import defaultdict
from copy import copy
from statistics import mean
from typing import Generator

from colorama import Fore, Style

MAX_RISK_LEVEL = 9
INPUT = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def main(lines: list[str]) -> int:
    coords = defaultdict(lambda: MAX_RISK_LEVEL + 1)
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            coords[(x, y)] = int(col)

    x_max = max(coords.keys())[0]
    y_max = max(coords.keys())[1]

    risks = traverse_cave(
        coords, x=0, y=0, risk=0, risks=set(), boundaries=(x_max, y_max), path=[]
    )

    return min(risks)


def traverse_cave(
    coords: defaultdict[tuple[int, int], int],
    x: int,
    y: int,
    risk: int,
    risks: set[int],
    boundaries: tuple[int, int],
    path: list[tuple[int, int]],
) -> set[int]:
    x_max, y_max = boundaries
    for neigh in get_neighbors(x, y, coords):
        if neigh[0] <= x_max and neigh[1] <= y_max:
            risk += coords[neigh]
            if is_risk_smaller(risk, risks):
                if neigh[0] == x_max and neigh[1] == y_max:
                    path.append(neigh)
                    risks.add(risk)
                    print_path(coords, copy(path))
                    path = []
                else:
                    path.append(neigh)
                    risks = traverse_cave(coords, *neigh, risk, risks, boundaries, path)
        path.pop() if path else False
    return risks


def get_neighbors(
    x: int, y: int, coords: defaultdict[tuple[int, int], int]
) -> Generator[tuple[int, int], None, None]:
    if mean([coords[x, y + 1] + coords[x, y + 2]]) <= mean(
        [coords[x + 1, y] + coords[x + 2, y]]
    ):
        yield x, y + 1
        yield x + 1, y
    else:
        yield x + 1, y
        yield x, y + 1


def is_risk_smaller(risk: int, risks: set[int]) -> bool:
    try:
        return risk < min(risks)
    except ValueError:
        return True


def print_path(
    coords: defaultdict[tuple[int, int], int], path: list[tuple[int, int]]
) -> None:
    path.append((0, 0))
    y0 = 0
    for x, y in coords:
        if y > y0:  # go to the next line
            print(Style.RESET_ALL)
            y0 = y
        if coords[(x, y)] < 10:
            if (x, y) in path:
                color = Fore.RED
            else:
                color = Fore.WHITE
            print(color + str(coords[(x, y)]), end="")
    print(Style.RESET_ALL)


def parse_input_file() -> list[str]:
    with open("day15/input.txt", "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}\n")

    # real_result = main(parse_input_file())
    # print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT.splitlines()) == 40


def test_main_real_data():
    assert main(parse_input_file()) == -1
