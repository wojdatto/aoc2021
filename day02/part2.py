def main():
    horizontal_pozition = 0
    depth = 0
    aim = 0

    with open("input.txt", "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(line.strip())

    commands = lines

    for cmd in commands:

        instruction, amount = cmd.split()
        amount = int(amount)

        if instruction == "forward":
            horizontal_pozition += amount
            depth += aim * amount
        elif instruction == "down":
            aim += amount
        elif instruction == "up":
            aim -= amount
        else:
            raise NotImplemented

        print(f"{instruction=}\t{amount=}\t{horizontal_pozition=}\t{depth=}\t{aim=}")

    print(f"\n{horizontal_pozition=}, {depth=}")

    print(f"\n{horizontal_pozition*depth=}")

        

if __name__ == "__main__":
    main()
