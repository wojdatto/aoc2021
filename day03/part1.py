INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def main(lines: list[str]):
    num_of_bits = len(lines[0])
    bits: list[list[str]] = [[] for i in range(num_of_bits)]

    for line in lines:
        for idx, bit in enumerate(line):
            bits[idx].append(bit)

    gamma_str = ""
    epsilon_str = ""

    for column in bits:
        gamma_str += more_common(column)
        epsilon_str += less_common(column)

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    print(f"{gamma_str=}, {epsilon_str=}")
    print(f"{gamma=}, {epsilon=}")
    print(f"{gamma*epsilon=}")

    return gamma * epsilon


def less_common(data: list[str]) -> str:
    if more_common(data) == "0":
        return "1"
    return "0"


def more_common(data: list[str]) -> str:
    if data.count("0") > data.count("1"):
        return "0"
    return "1"


def parse_input() -> list[str]:
    with open("day03/input.txt", "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    assert main(INPUT.splitlines()) == 198


def test_main_real_data():
    assert main(parse_input()) == 3687446


if __name__ == "__main__":
    test_result = main(INPUT.splitlines())
    print(f"{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
