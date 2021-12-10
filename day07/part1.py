from statistics import median

INPUT = "16,1,2,0,4,2,7,1,2,14"


def main(numbers: list[int]) -> int:
    target = int(median(numbers))
    return compute_spent_fuel(numbers, target)


def compute_spent_fuel(numbers: list[int], target: int) -> int:
    return sum(abs(n - target) for n in numbers)


def parse_input() -> list[int]:
    with open("day07/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    assert main([int(i) for i in INPUT.split(",")]) == 37


def test_main_real_data():
    assert main(parse_input()) == 347509


if __name__ == "__main__":
    test_result = main([int(i) for i in INPUT.split(",")])
    print(f"{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
