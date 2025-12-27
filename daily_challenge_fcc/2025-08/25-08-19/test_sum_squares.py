from sum_squares import sum_of_squares
import unittest

"""
Tests

Waiting: 1. sum_of_squares(5) should return 55.
Waiting: 2. sum_of_squares(10) should return 385.
Waiting: 3. sum_of_squares(25) should return 5525.
Waiting: 4. sum_of_squares(500) should return 41791750.
Waiting: 5. sum_of_squares(1000) should return 333833500.
"""
class TestSumOfSquares(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(5), 55)
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(sum_of_squares(25), 5525)
        self.assertEqual(sum_of_squares(500), 41791750)
        self.assertEqual(sum_of_squares(1000), 333833500)
