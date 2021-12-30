import itertools
from pathlib import Path

import pytest

INPUT = """\
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
"""

INPUT2 = """\
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
"""


def main(s: list[str]) -> int:
    turned_on: set[tuple[int, int, int]] = set()
    for line in s:
        state, points = line.split()
        x_s, y_s, z_s = points.split(",")
        x1, x2 = get_points(x_s)
        y1, y2 = get_points(y_s)
        z1, z2 = get_points(z_s)
        if any([n > 50 or n < -50 for n in (x1, x2, y1, y2, z1, z2)]):
            break
        for x, y, z in itertools.product(
            range(min(x1, x2), max(x1, x2) + 1),
            range(min(y1, y2), max(y1, y2) + 1),
            range(min(z1, z2), max(z1, z2) + 1),
        ):
            if state == "on":
                turned_on.add((x, y, z))
            else:
                turned_on.discard((x, y, z))
    return len(turned_on)


def get_points(s: str) -> tuple[int, int]:
    p1s, p2s = s.split("..")
    p1 = int(p1s.partition("=")[-1])
    p2 = int(p2s)
    return p1, p2


def get_score(steps: int) -> int:
    return steps % 10 if steps % 10 > 0 else 10


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result = main(INPUT2.splitlines())
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (INPUT, 39),
        (INPUT2, 590784),
    ],
)
def test_main_example_data(test_input, expected):
    assert main(test_input.splitlines()) == expected


def test_main_real_data():
    assert main(parse_input_file()) == 556501
