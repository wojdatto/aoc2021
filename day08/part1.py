from collections import defaultdict

INPUT = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |\
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |\
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |\
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |\
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |\
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |\
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |\
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |\
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |\
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |\
fgae cfgab fg bagce
"""


def main(input_data: list[tuple[list[str], list[str]]]) -> int:
    sum_of_digits = 0
    for row in input_data:
        sum_of_digits += parse_single_row(*row)
    return sum_of_digits


def parse_single_row(input_digits: list[str], output_digits: list[str]) -> int:
    digits_encoding = decode_easy_digits(input_digits)
    instances_of_known_digits = 0

    for digit in output_digits:
        if sort_str(digit) in digits_encoding.values():
            instances_of_known_digits += 1

    return instances_of_known_digits


def decode_easy_digits(input_digits: list[str]) -> dict[int, str]:
    digits_encoding = defaultdict(str)

    for digit in sort_str_list(input_digits):
        if len(digit) == 2:
            digits_encoding[1] = digit
        elif len(digit) == 3:
            digits_encoding[7] = digit
        elif len(digit) == 4:
            digits_encoding[4] = digit
        elif len(digit) == 7:
            digits_encoding[8] = digit

    return digits_encoding


def sort_str_list(input_str_list) -> list[str]:
    return [sort_str(i) for i in input_str_list]


def sort_str(letters: str) -> str:
    return "".join(sorted(letters))


def parse_input_data(input_str: str) -> tuple[list[str], list[str]]:
    input_digits_str, _, output_digits_str = input_str.partition("|")
    return input_digits_str.split(), output_digits_str.split()


def parse_input_file() -> list[str]:
    with open("day08/input.txt", "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    test_input_parsed = [parse_input_data(row) for row in INPUT.splitlines()]
    assert main(test_input_parsed) == 26


if __name__ == "__main__":
    test_input_parsed = [parse_input_data(row) for row in INPUT.splitlines()]

    test_result = main(test_input_parsed)
    print(f"{test_result=}")

    real_input_parsed = [parse_input_data(row) for row in parse_input_file()]

    real_result = main(real_input_parsed)
    print(f"{real_result=}")
