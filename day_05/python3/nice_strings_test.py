import unittest
from nice_strings import validate
from nice_strings import validate2


class TestPartOne(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(validate('ugknbfddgicrmopn'), True)
        self.assertEqual(validate('aaa'), True)
        self.assertEqual(validate('jchzalrnumimnmhp'), False)
        self.assertEqual(validate('haegwjzuvuyypxyu'), False)
        self.assertEqual(validate('dvszwmarrgswjxmb'), False)


class TestPartTwo(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(validate2('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(validate2('xxyxx'), True)
        self.assertEqual(validate2('uurcxstgmygtbstg'), False)
        self.assertEqual(validate2('ieodomkazucvgmuy'), False)

if __name__ == '__main__':
    unittest.main()
