from sum_divisors import sum_divisors
import unittest


class TestSumDivisors(unittest.TestCase):
    def test_sum_divisors_6(self):
        self.assertEqual(sum_divisors(6), 12)

    def test_sum_divisors_13(self):
        self.assertEqual(sum_divisors(13), 14)

    def test_sum_divisors_28(self):
        self.assertEqual(sum_divisors(28), 56)

    def test_sum_divisors_84(self):
        self.assertEqual(sum_divisors(84), 224)

    def test_sum_divisors_549(self):
        self.assertEqual(sum_divisors(549), 806)

    def test_sum_divisors_9348(self):
        self.assertEqual(sum_divisors(9348), 23520)

if __name__ == '__main__':
    unittest.main()
