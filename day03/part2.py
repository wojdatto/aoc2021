def main(filename):
    lines = _read_file(filename)

    num_of_bits = len(lines[0])
    bits: list[list[str]] = [[] for i in range(num_of_bits)]

    for line in lines:
        for idx, bit in enumerate(line):
            bits[idx].append(bit)

    oxygen_str = ""
    included_values = []
    more_common_indices = [x for x in range(len(bits[0]))]
    for column in bits:
        for row_idx, bit in enumerate(column):
            if row_idx in more_common_indices:
                included_values.append(bit)

        oxygen_str += more_common(included_values)

        more_common_indices = [i for i, x in enumerate(column) if (x == more_common(included_values) and i in more_common_indices)]

        included_values = []

    oxygen = int(oxygen_str, 2)
    print(f"{oxygen_str=}")
    print(f"{oxygen=}")


    co2_str = ""
    included_values = []
    less_common_indices = [x for x in range(len(bits[0]))]
    for column in bits:
        for row_idx, bit in enumerate(column):
            if row_idx in less_common_indices:
                included_values.append(bit)

        if included_values.count("0") == 1:
            interesting_idx_list = [i for i, x in enumerate(column) if (x == less_common(included_values) and i in less_common_indices)]
            assert len(interesting_idx_list) == 1
            co2_str = lines[interesting_idx_list[0]]

        less_common_indices = [i for i, x in enumerate(column) if (x == less_common(included_values) and i in less_common_indices)]

        included_values = []

    co2 = int(co2_str, 2)
    print(f"{co2_str=}")
    print(f"{co2=}")

    print(f"{oxygen*co2=}")

    return oxygen * co2


def less_common(data: list[str]) -> str:
    if data.count("0") <= data.count("1"):
        return "0"
    return "1"


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
    assert main("day03/example_input.txt") == 230


if __name__ == "__main__":
    main("day03/input.txt")
