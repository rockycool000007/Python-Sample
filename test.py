import unittest
from run import addNumbers, subNumbers, mulNumbers, divNumbers


class TestFunctions(unittest.TestCase):
    def test_addNumbers(self):
        result = addNumbers(1, 2)
        self.assertEqual(result, 3)

    def test_subNumbers(self):
        result = subNumbers(3, 2)
        self.assertEqual(result, 1)

    def test_mulNumbers(self):
        result = mulNumbers(2, 2)
        self.assertEqual(result, 4)

    def test_divNumbers(self):
        result = divNumbers(4, 2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
