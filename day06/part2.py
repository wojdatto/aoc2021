from collections import defaultdict
from copy import copy

INPUT = "3,4,3,1,2"
DAYS_TO_SIMULATE = 256
MAX_FISH_AGE = 8


def main(data: list[int], days: int) -> int:
    fish = defaultdict(int)

    # Initialize the defaultdict with every day
    for i in range(MAX_FISH_AGE + 1):
        fish[i]

    for i in data:
        fish[i] += 1

    for _ in range(days):
        sum_to_add = copy(fish[0])

        for age in fish:
            if age == 6:
                fish[age] = fish[age + 1] + sum_to_add
            elif age == 8:
                fish[age] = sum_to_add
            else:
                fish[age] = fish[age + 1]

    return sum(fish.values())


def parse_input() -> list[int]:
    with open("day06/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    test_input = [int(i) for i in INPUT.split(",")]
    assert main(test_input, DAYS_TO_SIMULATE) == 26984457539


def test_main_real_data():
    assert main(parse_input(), DAYS_TO_SIMULATE) == 1710623015163


if __name__ == "__main__":
    test_result = main([int(i) for i in INPUT.split(",")], DAYS_TO_SIMULATE)
    print(f"{test_result=}")

    real_result = main(parse_input(), DAYS_TO_SIMULATE)
    print(f"{real_result=}")
