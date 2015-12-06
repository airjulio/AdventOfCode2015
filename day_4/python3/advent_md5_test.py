import unittest
from advent_md5 import *


class TestPartOne(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_md5('abcdef609043'), '000001dbbfa3a5c83a2d506429c7b00e')
        self.assertEqual(get_md5('pqrstuv1048970'), '000006136ef2ff3b291c85725f17325c')


if __name__ == '__main__':
    unittest.main()
