def main(filename):
    lines = _read_file(filename)

    num_of_bits = len(lines[0])
    bits: list[list[str]] = [[] for i in range(num_of_bits)]

    for line in lines:
        for idx, bit in enumerate(line):
            bits[idx].append(bit)

    oxygen_str = ""

    # previous_more_common = more_common(bits[0])
    # included_values = bits[0]
    included_values = []
    more_common_indices = [x for x in range(len(bits[0]))]
    for col_idx, column in enumerate(bits):
        for row_idx, bit in enumerate(column):
            if row_idx in more_common_indices:
                included_values.append(bit)

        oxygen_str += more_common(included_values)
        # current_more_common = more_common(included_values)

        more_common_indices = [i for i, x in enumerate(column) if (x == more_common(included_values) and i in more_common_indices)]

        included_values = []

        # # check next column
        # for index in more_common_indices:
        #     bits[col_idx+1]

        # included_values: list[str] = []
        # for bit in column:
        #     if bit == previous_more_common:
        #         included_values.append(bit)
            
        # oxygen_str += more_common(included_values)
        # previous_more_common = more_common(column)


    oxygen = int(oxygen_str, 2)

    print(f"{oxygen_str=}")
    print(f"{oxygen=}")

    return oxygen


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
    assert main("day03/example_input.txt") == 23


if __name__ == "__main__":
    main("day03/example_input.txt")
