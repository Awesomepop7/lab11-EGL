# https://github.com/Awesomepop7/lab11-EGL
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(1, -2), -1)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-1, 2), -3)
        self.assertEqual(subtract(1, -2), 3)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(1, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 6), 3)
        self.assertEqual(divide(-2, -6), 3)
        self.assertEqual(divide(-2, 0), 0)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(1000, 10), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(3, 0), 3)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)


# Do not touch this
if __name__ == "__main__":
    unittest.main()