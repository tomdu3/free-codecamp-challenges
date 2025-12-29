from pairwise import pairwise
import unittest

"""
Tests

Waiting: 1. pairwise([2, 3, 4, 6, 8], 10) should return 9.
Waiting: 2. pairwise([4, 1, 5, 2, 6, 3], 7) should return 15.
Waiting: 3. pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) should return 22.
Waiting: 4. pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) should return 10.
"""

class TestPairwise(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(pairwise([2, 3, 4, 6, 8], 10), 9)
        self.assertEqual(pairwise([4, 1, 5, 2, 6, 3], 7), 15)
        self.assertEqual(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24), 10)
    def test_mixed_numbers(self):
        self.assertEqual(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20), 22)


if __name__ == '__main__':
    unittest.main()
