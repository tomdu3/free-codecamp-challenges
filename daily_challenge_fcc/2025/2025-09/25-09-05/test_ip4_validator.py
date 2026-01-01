from ipv4_validator import is_valid_ipv4
import unittest

"""
Tests

Waiting: 1. is_valid_ipv4("192.168.1.1") should return True.
Waiting: 2. is_valid_ipv4("0.0.0.0") should return True.
Waiting: 3. is_valid_ipv4("255.01.50.111") should return False.
Waiting: 4. is_valid_ipv4("255.00.50.111") should return False.
Waiting: 5. is_valid_ipv4("256.101.50.115") should return False.
Waiting: 6. is_valid_ipv4("192.168.101.") should return False.
Waiting: 7. is_valid_ipv4("192168145213") should return False.
"""

class TestIP4Validator(unittest.TestCase):
    def test_is_valid_ipv4(self):
        self.assertTrue(is_valid_ipv4("192.168.1.1"))
        self.assertTrue(is_valid_ipv4("0.0.0.0"))
        self.assertFalse(is_valid_ipv4("255.01.50.111"))
        self.assertFalse(is_valid_ipv4("255.00.50.111"))
        self.assertFalse(is_valid_ipv4("256.101.50.115"))
        self.assertFalse(is_valid_ipv4("192.168.101."))
        self.assertFalse(is_valid_ipv4("192168145213"))

if __name__ == "__main__":
    unittest.main()
