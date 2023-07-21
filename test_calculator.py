# test_calculator.py
import unittest
from calculator import divide_numbers

class TestCalculator(unittest.TestCase):

    def test_divide_numbers(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(8, 0)

if __name__ == '__main__':
    unittest.main()
