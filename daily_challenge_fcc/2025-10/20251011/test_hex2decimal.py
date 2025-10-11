import unittest
from hex2decimal import hex_to_decimal

class TestHexToDecimal(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(hex_to_decimal("A"), 10)

    def test_two_digits(self):
        self.assertEqual(hex_to_decimal("15"), 21)
        self.assertEqual(hex_to_decimal("2E"), 46)
        self.assertEqual(hex_to_decimal("FF"), 255)

    def test_three_digits(self):
        self.assertEqual(hex_to_decimal("A3F"), 2623)

    def test_zero(self):
        self.assertEqual(hex_to_decimal("0"), 0)

    def test_large_hex(self):
        self.assertEqual(hex_to_decimal("123ABC"), 1194684)

if __name__ == "__main__":
    unittest.main()