from pathlib import Path

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
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

PARING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def main(input_lines: list[str]) -> int:
    lines_scoring: list[int] = []

    for line in input_lines:
        try:
            completing_part = find_missing_part(line)
        except ValueError:
            pass
        else:
            score = 0
            for char in completing_part:
                score *= 5
                score += SCORING[char]
            lines_scoring.append(score)

    return sorted(lines_scoring)[int(len(lines_scoring) / 2)]


def find_missing_part(line: str) -> str:
    line_simplified = simplify_line(line)
    for char in line_simplified:
        if char in SCORING.keys():
            raise ValueError("Line is illegal")
    return complete_line(line_simplified)


def complete_line(line: str) -> str:
    completing_part = ""
    for char in reversed(line):
        completing_part += PARING[char]
    return completing_part


def simplify_line(line: str) -> str:
    original_line = line
    replacements = ("()", "[]", "{}", "<>")

    for rpl in replacements:
        line = line.replace(rpl, "")

    if line != original_line:
        line = simplify_line(line)

    return line


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 288957


def test_main_real_data():
    assert main(parse_input_file()) == 2858785164


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
