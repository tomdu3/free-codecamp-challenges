import unittest
from caught_speeding import speeding
import math

class TestSpeeding(unittest.TestCase):

    def test_no_speeding(self):
        self.assertEqual(speeding([50, 60, 55], 60), [0, 0])

    def test_some_speeding(self):
        self.assertEqual(speeding([58, 50, 60, 55], 55), [2, 4])

    def test_multiple_speeders(self):
        self.assertEqual(speeding([61, 81, 74, 88, 65, 71, 68], 70), [4, 8.5])

    def test_high_limits(self):
        self.assertEqual(speeding([100, 105, 95, 102], 100), [2, 3.5])

    def test_one_extreme_speeder(self):
        self.assertEqual(speeding([40, 45, 44, 50, 112, 39], 55), [1, 57])

    # Additional tests
    def test_all_below_limit(self):
        self.assertEqual(speeding([10, 20, 30], 40), [0, 0])

    def test_all_at_limit(self):
        self.assertEqual(speeding([55, 55, 55], 55), [0, 0])

    def test_all_above_limit(self):
        result = speeding([70, 80, 90], 60)
        self.assertEqual(result[0], 3)
        self.assertAlmostEqual(result[1], 20)

    def test_empty_list(self):
        self.assertEqual(speeding([], 50), [0, 0])

    def test_negative_speeds(self):
        self.assertEqual(speeding([-10, -5, 0, 5], 0), [1, 5])

    def test_limit_zero(self):
        self.assertEqual(speeding([1, 2, 3], 0), [3, 2])

    def test_floats(self):
        result = speeding([60.5, 61.2, 59.9], 60)
        self.assertEqual(result[0], 2)
        self.assertTrue(math.isclose(result[1], 0.85, rel_tol=1e-9))

if __name__ == '__main__':
    unittest.main()