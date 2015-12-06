import unittest
from read_input import *
from part_one import calculate_paper
from part_two import calculate_ribbon


class TestPartOne(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_paper(Box(2, 3, 4)), 58)
        self.assertEqual(calculate_paper(Box(1, 1, 10)), 43)


class TestPartTwo(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_ribbon(Box(2, 3, 4)), 34)
        self.assertEqual(calculate_ribbon(Box(1, 1, 10)), 14)

if __name__ == '__main__':
    unittest.main()
