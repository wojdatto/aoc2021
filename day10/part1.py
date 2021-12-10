from __future__ import annotations

from collections import defaultdict

INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

SCORING = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def main(input_lines: list[str]) -> int:
    illegal_chars = defaultdict(int)
    incomplete_lines = 0

    for line in input_lines:
        try:
            illegal_chars[find_illegal_char(line)] += 1
        except ValueError:
            incomplete_lines += 1

    return calculate_score(illegal_chars)


def find_illegal_char(line: str) -> str | None:
    line_simplified = simplify_line(line)
    for char in line_simplified:
        if char in SCORING.keys():
            return char
    raise ValueError("Line is legal but incomplete")


def simplify_line(line: str) -> str:
    original_line = line
    replacements = ("()", "[]", "{}", "<>")

    for rpl in replacements:
        line = line.replace(rpl, "")

    if line != original_line:
        line = simplify_line(line)

    return line


def calculate_score(illegal_chars: dict[str, int]) -> int:
    score = 0
    for char, number in illegal_chars.items():
        score += SCORING[char] * number
    return score


def parse_input_file() -> list[str]:
    with open("day10/input.txt", "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 26397


def test_main_real_data():
    assert main(parse_input_file()) == 323691


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
