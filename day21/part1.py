import itertools
from pathlib import Path

INPUT = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""


def main(s: list[str]) -> int:
    p1 = int(s[0][-1])
    p2 = int(s[1][-1])
    p1_score = p2_score = 0

    roll = itertools.cycle(range(1, 101))
    rolls = 0
    while True:
        p1 += sum([next(roll) for _ in range(3)])
        p1_score += get_score(p1)
        rolls += 3
        if p1_score >= 1000:
            break

        p2 += sum([next(roll) for _ in range(3)])
        p2_score += get_score(p2)
        rolls += 3
        if p2_score >= 1000:
            break

    return min(p1_score, p2_score) * rolls


def get_score(steps: int) -> int:
    return steps % 10 if steps % 10 > 0 else 10


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT.splitlines()) == 739785


def test_main_real_data():
    assert main(parse_input_file()) == 926610
