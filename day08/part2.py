from copy import copy
from pathlib import Path

INPUT = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
"""
INPUT = INPUT.replace("|\n", "|")


def main(input_data: list[tuple[list[str], list[str]]]) -> int:
    sum_of_digits = 0
    for row in input_data:
        sum_of_digits += parse_single_row(*row)
    return sum_of_digits


def parse_single_row(input_digits: list[str], output_digits: list[str]) -> int:
    encoding = decode_easy_digits(input_digits)

    remaining_digits_6_char = [digit for digit in input_digits if len(digit) == 6]
    encoding = decode_6_char_digits(remaining_digits_6_char, copy(encoding))

    remaining_digits_5_char = [digit for digit in input_digits if len(digit) == 5]
    encoding = decode_5_char_digits(remaining_digits_5_char, copy(encoding))

    return decode_ouptut_number(output_digits, encoding)


def decode_easy_digits(input_digits: list[str]) -> dict[int, str]:
    encoding = {}

    for digit in sort_str_list(input_digits):
        if len(digit) == 2:
            encoding[1] = digit
        elif len(digit) == 3:
            encoding[7] = digit
        elif len(digit) == 4:
            encoding[4] = digit
        elif len(digit) == 7:
            encoding[8] = digit

    return encoding


def decode_6_char_digits(
    input_digits: list[str], encoding: dict[int, str]
) -> dict[int, str]:
    for digit in sort_str_list(input_digits):
        if is_str_in_other(encoding[4], digit):
            encoding[9] = digit
        elif is_str_in_other(digit, encoding[8]) and not is_str_in_other(
            encoding[1], digit
        ):
            encoding[6] = digit
        else:
            encoding[0] = digit

    return encoding


def decode_5_char_digits(
    input_digits: list[str], encoding: dict[int, str]
) -> dict[int, str]:
    for digit in sort_str_list(input_digits):
        if is_str_in_other(digit, encoding[6]):
            encoding[5] = digit
        elif is_str_in_other(digit, encoding[9]):
            encoding[3] = digit
        else:
            encoding[2] = digit

    return encoding


def decode_ouptut_number(output_digits: list[str], encoding: dict[int, str]) -> int:
    decoded_digit_str = ""
    for digit in sort_str_list(output_digits):
        for key, value in encoding.items():
            if digit == value:
                decoded_digit_str += str(key)
    return int(decoded_digit_str)


def is_str_in_other(tested_str: str, bigger_str: str) -> bool:
    for char in tested_str:
        if char not in bigger_str:
            return False
    return True


def sort_str_list(input_str_list) -> list[str]:
    return [sort_str(i) for i in input_str_list]


def sort_str(letters: str) -> str:
    return "".join(sorted(letters))


def parse_input_data(input_str: str) -> tuple[list[str], list[str]]:
    input_digits_str, _, output_digits_str = input_str.partition("|")
    return input_digits_str.split(), output_digits_str.split()


def parse_input_file() -> list[str]:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().splitlines()


def test_main_example_data():
    test_input_parsed = [parse_input_data(row) for row in INPUT.splitlines()]
    assert main(test_input_parsed) == 61229


def test_main_real_data():
    test_input_parsed = [parse_input_data(row) for row in parse_input_file()]
    assert main(test_input_parsed) == 1068933


if __name__ == "__main__":
    test_input_parsed = [parse_input_data(row) for row in INPUT.splitlines()]
    test_result = main(test_input_parsed)
    print(f"{test_result=}")

    real_input_parsed = [parse_input_data(row) for row in parse_input_file()]
    real_result = main(real_input_parsed)
    print(f"{real_result=}")
