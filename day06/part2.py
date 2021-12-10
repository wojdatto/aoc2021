from collections import Counter

INPUT = "3,4,3,1,2"
DAYS_TO_SIMULATE = 256
MAX_FISH_AGE = 8


def main(data: list[int]) -> int:
    fish = Counter(n for n in data)

    for _ in range(DAYS_TO_SIMULATE):
        fish_new = Counter({6: fish[0], 8: fish[0]})
        for key, val in fish.items():
            if key > 0:
                fish_new[key - 1] += val
        fish = fish_new
    return sum(fish.values())


def parse_input() -> list[int]:
    with open("day06/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    test_input = [int(i) for i in INPUT.split(",")]
    assert main(test_input) == 26984457539


def test_main_real_data():
    assert main(parse_input()) == 1710623015163


if __name__ == "__main__":
    test_result = main([int(i) for i in INPUT.split(",")])
    print(f"{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
