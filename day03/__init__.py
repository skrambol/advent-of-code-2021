import operator
from typing import List, Tuple


def count_bits_at_position(bitstrings: List[str], position: int) -> Tuple[int, int]:
    """
    returns a tuple of the occurence of bits from a given bitstrings and position

    bitstrings: List of bitstrings, assumed to be of same length
    position: int, 0-based positioning/indexing
    """
    count: List[int] = [0, 0]

    for bitstring in bitstrings:
        bit: int = int(bitstring[position])
        count[bit] = count[bit] + 1

    return (count[0], count[1])

def get_bit_from_count(count: Tuple[int,int], condition: str) -> str:
    """
    returns the bit given a count and a condition

    count: Tuple of bit count
    condition: str
        "gamma": performs count[0] > count[1]
        "epsilon": performs count[0] <= count[1]
        "oxygen": performs count[0] > count[1]
        "co2": performs count[0] <= count[1]

    # https://stackoverflow.com/a/36852350
    """
    lookup = {
        "gamma": operator.gt,
        "epsilon": operator.le,
        "oxygen": operator.gt,
        "co2": operator.le,
    }

    return "0" if lookup[condition](count[0], count[1]) else "1"


class PartOne():
    @staticmethod
    def get_rate(diagnostics: List[str], rating: str):
        rate: str = ""

        for i in range(len(diagnostics[0])):
            count: Tuple[int, int] = count_bits_at_position(diagnostics, i)
            rate = rate + get_bit_from_count(count, rating)

        return rate

    @staticmethod
    def get_power_consumption(gamma_rate: str, epsilon_rate: str) -> int:
        """
        returns the power consumption based on gamma rate and epsilon rate

        gamma_rate: bitstring, to be converted to its decimal counterpart
        epsilon_rate: bitstring, to be converted to its decimal counterpart
        """
        gamma: int = int(gamma_rate,2)
        epsilon: int = int(epsilon_rate,2)

        return gamma * epsilon

class PartTwo():
    @staticmethod
    def get_rate(diagnostics: List[str], rating: str) -> str:
        for i in range(len(diagnostics[0])):
            count = count_bits_at_position(diagnostics, i)
            bit: str = get_bit_from_count(count, rating)
            diagnostics = [line for line in diagnostics if line[i] == bit]

            if len(diagnostics) == 1:
                return diagnostics[0]

        return diagnostics[0]

    @staticmethod
    def get_life_support_rating(oxygen_rating: str, co2_rating: str) -> int:
        oxygen: int = int(oxygen_rating,2)
        co2: int = int(co2_rating,2)

        return oxygen * co2
