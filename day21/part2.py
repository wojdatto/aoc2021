import functools
import itertools
from collections import Counter
from pathlib import Path

INPUT = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""


def main(s: list[str]) -> int:
    p1 = int(s[0][-1])
    p2 = int(s[1][-1])

    rolls = Counter(
        sum(points) for points in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3))
    )

    @functools.cache
    def compute_wins(
        p1_pos: int, p1_score: int, p2_pos: int, p2_score: int
    ) -> tuple[int, int]:
        p1_wins = p2_wins = 0
        for turn_steps, times_rolled in rolls.items():
            new_p1_pos = get_score(p1_pos + turn_steps)
            new_p1_score = p1_score + new_p1_pos

            if new_p1_score >= 21:
                p1_wins += times_rolled
            else:
                # flip players to account for player 2 turn
                tmp_p2_wins, tmp_p1_wins = compute_wins(
                    p2_pos,
                    p2_score,
                    new_p1_pos,
                    new_p1_score,
                )
                p1_wins += tmp_p1_wins * times_rolled
                p2_wins += tmp_p2_wins * times_rolled

        return p1_wins, p2_wins

    return max(compute_wins(p1, 0, p2, 0))


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
    assert main(INPUT.splitlines()) == 444356092776315


def test_main_real_data():
    assert main(parse_input_file()) == 146854918035875
