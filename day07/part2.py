from collections import defaultdict

import pytest

INPUT = "16,1,2,0,4,2,7,1,2,14"


def main(data) -> int:
    cnt = defaultdict(int)
    for number in data:
        cnt[number] += 1

    fuel_spent_min = -1
    for target in range(max(cnt.keys())):
        fuel_spent = 0
        for number in data:
            fuel_spent += sum([i for i in range(abs(number - target) + 1)])

        if fuel_spent_min == -1:
            fuel_spent_min = fuel_spent
        elif fuel_spent < fuel_spent_min:
            fuel_spent_min = fuel_spent

    return fuel_spent_min


def parse_input() -> list[int]:
    with open("day07/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    assert main([int(i) for i in INPUT.split(",")]) == 168


@pytest.mark.slow
def test_main_real_data():
    assert main(parse_input()) == 98257206


if __name__ == "__main__":
    test_result = main([int(i) for i in INPUT.split(",")])
    print(f"{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
