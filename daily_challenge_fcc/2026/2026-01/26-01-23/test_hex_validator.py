from hex_validator import is_valid_hex
import unittest


class TestHexValidator(unittest.TestCase):
    def test_is_valid_hex(self):
        self.assertTrue(is_valid_hex("#123"))
        self.assertTrue(is_valid_hex("#123abc"))
        self.assertTrue(is_valid_hex("#ABCDEF"))
        self.assertTrue(is_valid_hex("#0a1B2c"))
        self.assertFalse(is_valid_hex("#12G"))
        self.assertFalse(is_valid_hex("#1234567"))
        self.assertFalse(is_valid_hex("#12 3"))
        self.assertFalse(is_valid_hex("fff"))

if __name__ == "__main__":
    unittest.main()
