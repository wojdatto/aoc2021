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

    def print_all(self) -> None:
        for _ in range(self.min_x, self.max_x):
            for _ in range(self.min_y, self.max_y):
                print(".", end="")
            print()


def main(lines: list[str]):
    coords = Coordinates()

    for line in lines:
        x1y1, _, x2y2 = line.partition(" -> ")
        x1, y1, x2, y2 = ",".join([x1y1, x2y2]).split(",")

        coords.x1.append(int(x1))
        coords.x2.append(int(x2))
        coords.y1.append(int(y1))
        coords.y2.append(int(y2))

    overlapping = defaultdict(int)
    for x1, y1, x2, y2 in zip(coords.x1, coords.y1, coords.x2, coords.y2):
        if x1 == x2 or y1 == y2:
            overlapping[(x1, y1)] += 1
            overlapping[(x2, y2)] += 1

    print(overlapping)


def parse_input() -> list[str]:
    with open("day05/input.txt", "r") as file:
        lines = file.read().splitlines()
    return lines


if __name__ == "__main__":
    main(INPUT.splitlines())
