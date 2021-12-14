import itertools
from collections import Counter, defaultdict

INPUT_SMALL = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

INPUT_MEDIUM = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

INPUT_BIG = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def main(lines: list[str]) -> int:
    lines_split = [line.split("-") for line in lines]
    caves = set(itertools.chain(*lines_split))
    connections = defaultdict(set)

    for cave in caves:
        for entry, out in lines_split:
            if cave == entry:
                connections[cave].add(out)
            elif cave == out:
                connections[cave].add(entry)

    paths: set[str] = set()
    path = "start"
    paths = find_way(paths, connections, path)

    return len(paths)


def find_way(
    paths: set[str], connections: defaultdict[str, set[str]], path: str
) -> set[str]:
    path_list = path.split(",")
    destinations = connections[path_list[-1]]
    for dest in sorted(destinations):
        proposal = path + "," + dest
        if dest == "start":
            continue
        elif dest.lower() in path_list:
            C = Counter(path_list)
            if all([C[key] < 2 for key in C.keys() if key == key.lower()]):
                paths = find_way(paths, connections, proposal)
        elif dest == "end":
            if proposal not in paths:
                paths.add(proposal)
        else:
            paths = find_way(paths, connections, proposal)

    return paths


def parse_input_file() -> list[str]:
    with open("day12/input.txt", "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    test_result_small = main(INPUT_SMALL.splitlines())
    print(f"{test_result_small=}")

    test_result_medium = main(INPUT_MEDIUM.splitlines())
    print(f"{test_result_medium=}")

    test_result_big = main(INPUT_BIG.splitlines())
    print(f"{test_result_big=}")

    real_result = main(parse_input_file())
    print(f"{real_result=}")


def test_main_example_data_small():
    assert main(INPUT_SMALL.splitlines()) == 36


def test_main_example_data_medium():
    assert main(INPUT_MEDIUM.splitlines()) == 103


def test_main_example_data_big():
    assert main(INPUT_BIG.splitlines()) == 3509


def test_main_real_data():
    assert main(parse_input_file()) == 91292
