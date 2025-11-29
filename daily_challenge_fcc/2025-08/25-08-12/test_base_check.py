import unittest
from base_check import is_valid_number

class TestIsValidNumber(unittest.TestCase):
    def test_binary_valid(self):
        self.assertTrue(is_valid_number("10101", 2))

    def test_binary_invalid(self):
        self.assertFalse(is_valid_number("10201", 2))

    def test_octal_valid(self):
        self.assertTrue(is_valid_number("76543210", 8))

    def test_octal_invalid(self):
        self.assertFalse(is_valid_number("9876543210", 8))

    def test_decimal_valid(self):
        self.assertTrue(is_valid_number("9876543210", 10))

    def test_decimal_invalid_alpha(self):
        self.assertFalse(is_valid_number("ABC", 10))

    def test_hex_valid_alpha(self):
        self.assertTrue(is_valid_number("ABC", 16))

    def test_base36_valid_z(self):
        self.assertTrue(is_valid_number("Z", 36))

    def test_base20_valid_abc(self):
        self.assertTrue(is_valid_number("ABC", 20))

    def test_hex_valid_mixed(self):
        self.assertTrue(is_valid_number("4B4BA9", 16))

    def test_hex_invalid_g(self):
        self.assertFalse(is_valid_number("5G3F8F", 16))

    def test_base17_valid_g(self):
        self.assertTrue(is_valid_number("5G3F8F", 17))

    def test_decimal_invalid_lower(self):
        self.assertFalse(is_valid_number("abc", 10))

    def test_hex_valid_lower(self):
        self.assertTrue(is_valid_number("abc", 16))

    def test_hex_valid_mixed_case(self):
        self.assertTrue(is_valid_number("AbC", 16))

    def test_base36_valid_lower_z(self):
        self.assertTrue(is_valid_number("z", 36))

if __name__ == "__main__":
    unittest.main()