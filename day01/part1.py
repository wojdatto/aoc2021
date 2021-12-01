"""https://adventofcode.com/2021/day/1"""


def main():
    with open("inputfile", "r") as file:
        lines = file.readlines()

    measurement = 0
    increased = 0
    
    lines = [int(line.strip()) for line in lines]
    
    for line in lines:

        if line > measurement:
            increased += 1

        measurement = line

    increased -= 1  # we have to ignore the first increase

    print(f"{increased=}")



if __name__ == "__main__":
    main()
