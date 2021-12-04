import unittest
from . import PartOne, PartTwo, count_bits_at_position, get_bit_from_count

sample1 = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

class UtilTest(unittest.TestCase):
    def test_count_bits_at_position(self):
        result = count_bits_at_position(sample1, 0)
        self.assertEqual(result, (5,7))

        result = count_bits_at_position(sample1, 1)
        self.assertEqual(result, (7,5))

        result = count_bits_at_position(sample1, 2)
        self.assertEqual(result, (4,8))

    def test_get_bit_from_count(self):
        result = get_bit_from_count((5,7), "gamma")
        self.assertEqual(result, "1")

        result = get_bit_from_count((5,7), "epsilon")
        self.assertEqual(result, "0")

        result = get_bit_from_count((5,5), "oxygen")
        self.assertEqual(result, "1")

        result = get_bit_from_count((5,5), "co2")
        self.assertEqual(result, "0")

class PartOneTest(unittest.TestCase):
    def test_get_gamma_rate(self):
        result = PartOne.get_rate(sample1, "gamma")
        self.assertEqual(result, "10110")

    def test_get_epsilon_rate(self):
        result = PartOne.get_rate(sample1, "epsilon")
        self.assertEqual(result, "01001")

    def test_get_power_consumption(self):
        result = PartOne.get_power_consumption("10110", "01001")
        self.assertEqual(result, 198)

class PartTwoTest(unittest.TestCase):
    def test_get_oxygen_rating(self):
        result = PartTwo.get_rate(sample1, "oxygen")
        self.assertEqual(result, "10111")

    def test_get_co2_rating(self):
        result = PartTwo.get_rate(sample1, "co2")
        self.assertEqual(result, "01010")

if __name__ == "__main__":
    unittest.main()
