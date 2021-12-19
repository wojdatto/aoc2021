from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import pytest

INPUT = "04005AC33890"


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

    return evaluate(packet)


def evaluate(packet: Packet) -> int:
    if packet.type_id == 0:
        return sum(evaluate(p) for p in packet.packets)
    if packet.type_id == 1:
        return math.prod(evaluate(p) for p in packet.packets)
    if packet.type_id == 2:
        return min(evaluate(p) for p in packet.packets)
    if packet.type_id == 3:
        return max(evaluate(p) for p in packet.packets)
    if packet.type_id == 5:
        return int(evaluate(packet.packets[0]) > evaluate(packet.packets[1]))
    if packet.type_id == 6:
        return int(evaluate(packet.packets[0]) < evaluate(packet.packets[1]))
    if packet.type_id == 7:
        return int(evaluate(packet.packets[0]) == evaluate(packet.packets[1]))

    if packet.type_id == 4:
        return packet.value

    raise AssertionError


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
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_main_example_data(test_input, expected):
    assert main(test_input) == expected


def test_main_real_data():
    assert main(parse_input_file()) == 744953223228
