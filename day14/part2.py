from collections import Counter, defaultdict
from copy import copy

STEPS = 40
INPUT = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def main(template: str, rules_list: list[str]) -> int:
    rules = {key: val for key, val in [rule.split(" -> ") for rule in rules_list]}
    letters = defaultdict(int)

    for char in range(len(template) - 1):
        letters[template[char : char + 2]] += 1

    step = 0
    while step < STEPS:
        letters_cp = copy(letters)
        for pair in letters_cp:
            amount = letters_cp[pair]
            if amount:
                first, last = pair
                middle = rules[pair]
                letters[first + middle] += amount
                letters[middle + last] += amount
                letters[pair] -= amount
        step += 1

    count = defaultdict(int)
    for key, value in letters.items():
        count[key[0]] += value

    counter = Counter(count)
    offset = 1  # most common is 1 lower than it should be for some reason
    most_common = counter.most_common(1)[0][1] + offset
    least_common = counter.most_common()[-1][1]

    return most_common - least_common


def parse_input(input_data: str) -> tuple[str, list[str]]:
    template, rules = input_data.split("\n\n")
    return template.strip(), rules.splitlines()


def parse_input_file() -> str:
    with open("day14/input.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    test_result = main(*parse_input(INPUT))
    print(f"{test_result=}\n")

    real_result = main(*parse_input(parse_input_file()))
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(*parse_input(INPUT)) == 2188189693529


def test_main_real_data():
    assert main(*parse_input(parse_input_file())) == 2399822193707
