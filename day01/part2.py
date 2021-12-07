"""https://adventofcode.com/2021/day/1"""


def main():
    with open("day01/inputfile", "r") as file:
        lines = file.readlines()

    measurement = 0
    increased = 0

    lines = [int(line.strip()) for line in lines]
    lines_sum = [sum(lines[i:i+3]) for i, _ in enumerate(lines)]
    
    for line in lines_sum:

        if line > measurement:
            increased += 1

        measurement = line

    increased -= 1  # we have to ignore the first increase

    print(f"{increased=}")



if __name__ == "__main__":
    main()
