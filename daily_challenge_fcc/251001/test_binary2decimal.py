import unittest
from binary2decimal import to_decimal


class TestBinary2Decimal(unittest.TestCase):
    def test_binary2decimal(self):
        self.assertEqual(to_decimal("101"), 5)
        self.assertEqual(to_decimal("1010"), 10)
        self.assertEqual(to_decimal("10010"), 18)
        self.assertEqual(to_decimal("1010101"), 85)
