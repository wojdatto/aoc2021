from collections import Counter

STEPS = 10

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

    for _ in range(1, STEPS + 1):
        template = update_template(template, rules)

    count = Counter(template)
    most_common = count.most_common(1)[0][1]
    least_common = count.most_common()[-1][1]

    return most_common - least_common


def update_template(template: str, rules: dict[str, str]) -> str:
    template_new = ""
    for char in range(len(template) - 1):
        s = template[char : char + 2]
        template_new += s[0] + rules[s]
    return template_new + template[-1]


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
    assert main(*parse_input(INPUT)) == 1588


def test_main_real_data():
    assert main(*parse_input(parse_input_file())) == 2321
