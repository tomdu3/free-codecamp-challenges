from sum_strings import string_sum
import unittest

"""
Tests
Waiting:1. string_sum("3apples2bananas") should return 5.
Waiting:2. string_sum("10cats5dogs2birds") should return 17.
Waiting:3. string_sum("125344") should return 125344.
Waiting:4. string_sum("a1b20c300") should return 321.
Waiting:5. string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5") should return 1653.
"""


class TestStringSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(string_sum("3apples2bananas"), 5)

    def test_2(self):
        self.assertEqual(string_sum("10cats5dogs2birds"), 17)

    def test_3(self):
        self.assertEqual(string_sum("125344"), 125344)

    def test_4(self):
        self.assertEqual(string_sum("a1b20c300"), 321)

    def test_5(self):
        self.assertEqual(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"), 1653)


if __name__ == "__main__":
    unittest.main()
