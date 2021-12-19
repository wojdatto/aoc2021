from pathlib import Path

INPUT = "target area: x=20..30, y=-10..-5"
ITERATIONS = 220  # determined empirically :>


def main(s: str) -> int:
    x_min, x_max, y_min, y_max = parse_input_data(s)

    def simulate(vx, vy) -> bool:
        def make_step():
            nonlocal x, y
            nonlocal vx, vy

            x += vx
            y += vy

            if vx:
                vx = vx - 1 if x > 0 else vx + 1
            vy -= 1

        is_inside = False
        x, y = 0, 0
        vx, vy = vx, vy

        max_height = 0
        steps = 0
        while x not in range(x_min, x_max + 1) or y not in range(y_min, y_max + 1):
            make_step()
            max_height = y if y > max_height else max_height
            steps += 1

            if x > x_max:
                break
            if vx == 0 and y < y_min:
                break
        else:
            is_inside = True

        return is_inside

    initial_velocities: set[tuple[int, int]] = set()
    vx, vy = 1, 1
    for vx in range(ITERATIONS):
        for vy in range(-ITERATIONS // 2, ITERATIONS // 2):
            if simulate(vx=vx, vy=vy):
                initial_velocities.add((vx, vy))
    return len(initial_velocities)


def parse_input_data(s: str) -> tuple[int, int, int, int]:
    x, y = s.lstrip("target area: ").split(", ")
    x_min, x_max = x.lstrip("x=").split("..")
    y_min, y_max = y.lstrip("y=").split("..")
    return int(x_min), int(x_max), int(y_min), int(y_max)


def parse_input_file() -> str:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().strip()


if __name__ == "__main__":
    test_result = main(INPUT)
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


def test_main_example_data():
    assert main(INPUT) == 112


def test_main_real_data():
    assert main(parse_input_file()) == 1806
