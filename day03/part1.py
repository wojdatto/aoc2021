def main(filename):
    lines = _read_file(filename)

    num_of_bits = len(lines[0])
    bits: list[list[str]] = [[] for i in range(num_of_bits)]

    for line in lines:
        for idx, bit in enumerate(line):
            bits[idx].append(bit)

    gamma_str = ""
    epsilon_str = ""

    for row in bits:
        gamma_str += more_common(row)
        epsilon_str += less_common(row)

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


def _read_file(filename) -> list[str]:
    with open(filename, "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def test_main():
    assert main("example_input.txt") == 198


if __name__ == "__main__":
    main("input.txt")
