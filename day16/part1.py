from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

INPUT = "8A004A801A8002F478"


@dataclass
class Packet:
    version: int
    type_id: int
    value: int = -1
    packets: tuple[Packet, ...] = ()


def main(input_s: str) -> int:
    binary = get_binary_str(input_s)

    def parse_packet(idx: int) -> tuple[int, Packet]:
        def _read(n: int) -> int:
            nonlocal idx
            ret = int(binary[idx : idx + n], 2)
            idx += n
            return ret

        version = _read(3)
        type_id = _read(3)

        if type_id == 4:
            chunk = _read(5)
            value = chunk & 0b1111
            while chunk & 0b10000:
                chunk = _read(5)
                value <<= 4
                value += chunk & 0b1111

            return idx, Packet(version=version, type_id=type_id, value=value)

        else:
            mode = _read(1)

            if mode == 0:
                num_bits = _read(15)
                idx_start = idx
                idx = idx + num_bits
                packets = []
                while idx_start < idx:
                    idx_start, packet = parse_packet(idx_start)
                    packets.append(packet)

                ret = Packet(
                    version=version,
                    type_id=type_id,
                    packets=tuple(packets),
                )
                return idx, ret

            elif mode == 1:
                num_subpackets = _read(11)
                packets = []
                for _ in range(num_subpackets):
                    idx, packet = parse_packet(idx)
                    packets.append(packet)

                ret = Packet(
                    version=version,
                    type_id=type_id,
                    packets=tuple(packets),
                )
                return idx, ret

            else:
                raise AssertionError

    _, packet = parse_packet(0)
    todo = [packet]
    version_sum = 0
    while todo:
        p = todo.pop()
        version_sum += p.version
        todo.extend(p.packets)

    return version_sum


def get_binary_str(input_s: str) -> str:
    binary = ""
    for c in input_s.strip():
        binary += f"{int(c, 16):04b}"
    return binary


def parse_input_file() -> str:
    with open(Path(Path(__file__).parent, "input.txt"), "r") as file:
        return file.read().strip()


if __name__ == "__main__":
    test_result = main(INPUT)
    print(f"{test_result=}\n")

    real_result = main(parse_input_file())
    print(f"{real_result=}\n")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_main_example_data(test_input, expected):
    assert main(test_input) == expected


def test_main_real_data():
    assert main(parse_input_file()) == 957
