import unittest
from . import get_depth_change, count_depth_change, get_measurement_window

sample1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
answer1 = [None, True, True, True, False, True, True, True, False, True]
answer2 = [607, 618, 618, 617, 647, 716, 769, 792]

class Part1Test(unittest.TestCase):
    def test_get_depth_change(self):
        result = get_depth_change(sample1)
        self.assertListEqual(result, answer1)

    def test_count_depth_change(self):
        result = count_depth_change(get_depth_change(sample1))
        self.assertEqual(result, 7)

class Part2Test(unittest.TestCase):
    def test_get_measurement_window(self):
        result = get_measurement_window(sample1)
        self.assertListEqual(result, answer2)

    def test_count_depth_change(self):
        result = count_depth_change(get_depth_change(get_measurement_window(sample1)))
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
