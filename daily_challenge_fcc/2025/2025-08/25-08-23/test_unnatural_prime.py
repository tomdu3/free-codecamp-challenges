from unnatural_prime import is_unnatural_prime
import unittest

"""
Tests

Waiting: 1. is_unnatural_prime(1) should return False.
Waiting: 2. is_unnatural_prime(-1) should return False.
Waiting: 3. is_unnatural_prime(19) should return True.
Waiting: 4. is_unnatural_prime(-23) should return True.
Waiting: 5. is_unnatural_prime(0) should return False.
Waiting: 6. is_unnatural_prime(97) should return True.
Waiting: 7. is_unnatural_prime(-61) should return True.
Waiting: 8. is_unnatural_prime(99) should return False.
Waiting: 9. is_unnatural_prime(-44) should return False.
"""

class TestUnnaturalPrime(unittest.TestCase):
    def test_is_unnatural_prime(self):
        self.assertFalse(is_unnatural_prime(1))
        self.assertFalse(is_unnatural_prime(-1))
        self.assertTrue(is_unnatural_prime(19))
        self.assertTrue(is_unnatural_prime(-23))
        self.assertFalse(is_unnatural_prime(0))
        self.assertTrue(is_unnatural_prime(97))
        self.assertTrue(is_unnatural_prime(-61))
        self.assertFalse(is_unnatural_prime(99))
        self.assertFalse(is_unnatural_prime(-44))

if __name__ == '__main__':
    unittest.main()
    