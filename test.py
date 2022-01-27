"""
Test Metrics
"""

import unittest
from main import hypot

class HypotTest(unittest.TestCase):
    """Class HypotTest have 5 tests to check hypot function"""

    def test_2positive(self):
        """2 Positive"""
        res = hypot(8, 10)
        self.assertEqual(12.806248474865697, res)

    def test_zero(self):
        """ 2 Zero"""
        res = hypot(0, 0)
        self.assertEqual(0.0, res)

    def test_2negative(self):
        """2 Negative"""
        res = hypot(-1, -1)
        self.assertEqual(1.4142135623730951, res)

    def test_x_negative(self):
        """x is negative,  y is 0"""
        res = hypot(-5, 0)
        self.assertEqual(5.0, res)

    def test_y_negative(self):
        """y is negative,  x is 0"""
        res = hypot(0, -7)
        self.assertEqual(7.0, res)


if __name__ == "__main__":
    unittest.main()
