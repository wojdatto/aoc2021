import heapq
from pathlib import Path
from typing import Generator

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
    coords = {}
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            coords[(x, y)] = int(col)
    return traverse_cave(coords)


def traverse_cave(coords: dict[tuple[int, int], int]) -> int:
    x_max, y_max = max(coords)
    best_at: dict[tuple[int, int], int] = {}

    cost = -1
    todo = [(0, (0, 0))]
    while todo:
        cost, last_coord = heapq.heappop(todo)

        if last_coord in best_at and cost >= best_at[last_coord]:
            continue
        else:
            best_at[last_coord] = cost

        for candidate in get_neighbors(*last_coord):
            if candidate in coords:
                heapq.heappush(todo, (cost + coords[candidate], candidate))

        if last_coord == (x_max, y_max):
            break

    return cost


def get_neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT.splitlines()) == 40


def test_main_real_data():
    assert main(parse_input_file()) == 415
