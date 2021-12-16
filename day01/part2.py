from pathlib import Path

INPUT = """\
199
200
208
210
200
207
240
269
260
263
"""


def main(lines_str: list[str]):
    lines = [int(ln) for ln in lines_str]

    return sum(lines[i] > lines[i - 3] for i in range(3, len(lines)))


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 5


def test_main_real_data():
    assert main(parse_input_file()) == 1739


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
