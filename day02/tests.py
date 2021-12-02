import unittest
from . import PartOne, PartTwo

sample1 = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]

class PartOneTest(unittest.TestCase):
    def test_move_coordinates(self):
        result = PartOne.move_coordinates((0,0), ("forward", 2))
        self.assertTupleEqual(result, (2, 0))

        result = PartOne.move_coordinates((0,2), ("up", 1))
        self.assertTupleEqual(result, (0, 1))

        result = PartOne.move_coordinates((0,1), ("down", 2))
        self.assertTupleEqual(result, (0, 3))

    def test_get_final_position(self):
        position = (15, 10)
        self.assertEqual(PartOne.get_final_position(position), 150)

class PartTwoTest(unittest.TestCase):
    def test_move_coordinates(self):
        result = PartTwo.move_coordinates((0, 2, 0), ("up", 1))
        self.assertTupleEqual(result, (0, 2, -1))

        result = PartTwo.move_coordinates((0, 1, 0), ("down", 2))
        self.assertTupleEqual(result, (0, 1, 2))

        result = PartTwo.move_coordinates((5, 0, 5), ("forward", 8))
        self.assertTupleEqual(result, (13, 40, 5))

    def test_get_final_position(self):
        position = (15, 60, 10)
        self.assertEqual(PartTwo.get_final_position(position), 900)

if __name__ == "__main__":
    unittest.main()
