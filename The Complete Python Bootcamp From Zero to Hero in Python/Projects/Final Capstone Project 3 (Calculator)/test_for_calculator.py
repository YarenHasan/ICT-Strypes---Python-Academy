import unittest
from io import StringIO
import sys
from calculator import calc, main


class TestCalcFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc(3, 4, '+'), '3 + 4 = 7')

    def test_subtraction(self):
        self.assertEqual(calc(10, 6, '-'), '10 - 6 = 4')

    def test_multiplication(self):
        self.assertEqual(calc(2, 5, '*'), '2 * 5 = 10')

    def test_division(self):
        self.assertEqual(calc(9, 2, '/'), '9 / 2 = 4.5')

    def test_invalid_operator(self):
        self.assertEqual(calc(1, 2, '%'), 'Please only type one of these characters: "+, -, *, /"!')

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc(5, 0, '/')


if __name__ == '__main__':
    unittest.main()
