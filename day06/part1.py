INPUT = "3,4,3,1,2"
DAYS_TO_SIMULATE = 80
MAX_FISH_AGE = 8


def main(input_data, days: int):
    for _ in range(days):
        input_data = day_passed(input_data)
    return len(input_data)


def day_passed(data: list[int]) -> list[int]:
    spawned_fish = []
    for idx, _ in enumerate(data):
        data[idx] -= 1
        if data[idx] < 0:
            data[idx] = 6
            spawned_fish.append(MAX_FISH_AGE)
    return data + spawned_fish


def parse_input() -> list[int]:
    with open("day06/input.txt", "r") as file:
        data = file.readline().split(",")
    return [int(i) for i in data]


def test_main_example_data():
    test_input = [int(i) for i in INPUT.split(",")]
    assert main(test_input, DAYS_TO_SIMULATE) == 5934


if __name__ == "__main__":
    total_fish = main(parse_input(), DAYS_TO_SIMULATE)
    print(f"{total_fish=}")
