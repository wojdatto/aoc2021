INPUT = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

EXPECTED_EXAMPLE = """\
#####
#...#
#...#
#...#
#####
"""

EXPECTED_REAL = """\
..##..##...##....##.####.####.#..#.#..#
...#.#..#.#..#....#.#....#....#.#..#..#
...#.#....#..#....#.###..###..##...#..#
...#.#.##.####....#.#....#....#.#..#..#
#..#.#..#.#..#.#..#.#....#....#.#..#..#
.##...###.#..#..##..####.#....#..#..##.
"""


def main(points: list[str], folds: list[str]) -> str:
    coords = set()
    for line in points:
        x_s, y_s = line.split(",")
        x, y = int(x_s), int(y_s)
        coords.add((x, y))

    for fold_s in folds:
        axis, index_s = fold_s.split("=")
        index = int(index_s)

        coords_new = set()
        if axis == "y":

            for x, y in coords:
                if y > index:
                    diff = y - index
                    coords_new.add((x, index - diff))
        elif axis == "x":
            for x, y in coords:
                if x > index:
                    diff = x - index
                    coords_new.add((index - diff, y))
        else:
            raise AssertionError

        coords_folded = set()
        for x, y in coords | coords_new:
            if axis == "y":
                if y < index:
                    coords_folded.add((x, y))
            elif axis == "x":
                if x < index:
                    coords_folded.add((x, y))
        coords = coords_folded

    return render_text(coords)


def render_text(coords: set[tuple[int, int]]) -> str:
    x_max, _ = max(coords, key=lambda i: i[0])
    _, y_max = max(coords, key=lambda i: i[1])
    text = ""

    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if (x, y) in coords:
                text += "#"
            else:
                text += "."
        text += "\n"
    return text


def parse_input_file() -> str:
    with open("day13/input.txt", "r") as file:
        return file.read()


def parse_input(input_data: str) -> tuple[list[str], list[str]]:
    points, folds = input_data.split("\n\n")
    folds = [f.lstrip("fold along ") for f in folds.splitlines()]
    return points.splitlines(), folds


def test_main_example_data():
    assert main(*parse_input(INPUT)) == EXPECTED_EXAMPLE


def test_main_real_data():
    input_data = parse_input_file()
    assert main(*parse_input(input_data)) == EXPECTED_REAL


if __name__ == "__main__":
    test_result = main(*parse_input(INPUT))
    print(test_result)

    input_data = parse_input_file()
    real_result = main(*parse_input(input_data))
    print(real_result)
