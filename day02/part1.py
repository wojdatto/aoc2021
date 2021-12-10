INPUT = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def main(lines: list[str]):
    horizontal_position = 0
    depth = 0

    for cmd in lines:
        instruction, amount = cmd.split()
        amount = int(amount)

        if instruction == "forward":
            horizontal_position += amount
        elif instruction == "down":
            depth += amount
        elif instruction == "up":
            depth -= amount
        else:
            raise AssertionError("We shouldn't end here")

    return horizontal_position * depth


def parse_input_file() -> list[str]:
    with open("day02/input.txt", "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 150


def test_main_real_data():
    assert main(parse_input_file()) == 1693300


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")
