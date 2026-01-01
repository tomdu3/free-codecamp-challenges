from three_strikes import squares_with_three
import unittest

"""
Tests

Waiting: 1. squares_with_three(1) should return 0.
Waiting: 2. squares_with_three(10) should return 1.
Waiting: 3. squares_with_three(100) should return 19.
Waiting: 4. squares_with_three(1000) should return 326.
Waiting: 5. squares_with_three(10000) should return 4531.
"""

class TestSquaresWithThree(unittest.TestCase):
    def test_squares_with_three(self):
        self.assertEqual(squares_with_three(1), 0)
        self.assertEqual(squares_with_three(10), 1)
        self.assertEqual(squares_with_three(100), 19)
        self.assertEqual(squares_with_three(1000), 326)
        self.assertEqual(squares_with_three(10000), 4531)
