INPUT = "16,1,2,0,4,2,7,1,2,14"


def main(numbers: list[int]) -> int:
    return min(
        compute_spent_fuel(numbers, n) for n in range(min(numbers), max(numbers) + 1)
    )


def compute_spent_fuel(numbers: list[int], target: int) -> int:
    """Computes the sum of 1 + 2 + 3 + ... + n

    It is equal to (n * (n + 1)) // 2.
    """
    return sum(abs(n - target) * (abs(n - target) + 1) // 2 for n in numbers)


def parse_input() -> list[int]:
    with open("day07/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    assert main([int(i) for i in INPUT.split(",")]) == 168


def test_main_real_data():
    assert main(parse_input()) == 98257206


if __name__ == "__main__":
    test_result = main([int(i) for i in INPUT.split(",")])
    print(f"{test_result=}")

    real_result = main(parse_input())
    print(f"{real_result=}")
