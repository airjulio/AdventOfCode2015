import unittest
from house_grid_xmas import process_santa
from house_grid_xmas import process_robot


class TestPartOne(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(process_santa('>'), 2)
        self.assertEqual(process_santa('^>v<'), 4)
        self.assertEqual(process_santa('^v^v^v^v^v'), 2)


class TestPartTwo(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(process_robot('^v'), 3)
        self.assertEqual(process_robot('^>v<'), 3)
        self.assertEqual(process_robot('^v^v^v^v^v'), 11)

if __name__ == '__main__':
    unittest.main()
