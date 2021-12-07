from collections import defaultdict
from dataclasses import dataclass, field

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


@dataclass
class Coordinates:
    x1: list[int] = field(default_factory=list)
    x2: list[int] = field(default_factory=list)
    y1: list[int] = field(default_factory=list)
    y2: list[int] = field(default_factory=list)
    overlapping = defaultdict(int)

    @property
    def min_x(self) -> int:
        return min(set(self.x1 + self.x2))

    @property
    def min_y(self) -> int:
        return min(set(self.y1 + self.y2))

    @property
    def max_x(self) -> int:
        return max(set(self.x1 + self.x2))

    @property
    def max_y(self) -> int:
        return max(set(self.y1 + self.y2))

    @property
    def total_overlapping(self) -> int:
        return sum([1 for i in self.overlapping.values() if i > 1])

    def print_all(self) -> None:
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if self.overlapping[(x, y)]:
                    print(self.overlapping[(x, y)], end="")
                else:
                    print(".", end="")
            print()


def main(lines: list[str], is_test: bool = False):
    coords = parse_coords(lines)

    for x1, y1, x2, y2 in zip(coords.x1, coords.y1, coords.x2, coords.y2):
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coords.overlapping[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coords.overlapping[(i, y1)] += 1
        else:
            range_x = range(min(x1, x2), max(x1, x2) + 1)
            if x1 > x2:
                # to handle the situation when X coord in decreasing
                # and Y coord is not
                range_x = reversed(range_x)

            range_y = range(min(y1, y2), max(y1, y2) + 1)
            if y1 > y2:
                # to handle the situation when Y coord in decreasing
                # and X coord is not
                range_y = reversed(range_y)

            # When both are reversed this is the same if no one would be reversed

            for x, y in zip(range_x, range_y):
                coords.overlapping[(x, y)] += 1

    if is_test:
        coords.print_all()
    print(f"\n{coords.total_overlapping=}")


def parse_coords(data: list[str]) -> Coordinates:
    coords = Coordinates()
    for line in data:
        x1y1, _, x2y2 = line.partition(" -> ")
        x1, y1, x2, y2 = ",".join([x1y1, x2y2]).split(",")

        coords.x1.append(int(x1))
        coords.x2.append(int(x2))
        coords.y1.append(int(y1))
        coords.y2.append(int(y2))

    return coords


def parse_input() -> list[str]:
    with open("day05/input.txt", "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    # main(INPUT.splitlines(), is_test=True)
    main(parse_input())
