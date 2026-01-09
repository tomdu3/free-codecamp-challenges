from circular_prime import is_circular_prime
import unittest


class TestCircularPrime(unittest.TestCase):
    def test_is_circular_prime(self):
        self.assertTrue(is_circular_prime(197))
        self.assertFalse(is_circular_prime(23))
        self.assertTrue(is_circular_prime(13))
        self.assertFalse(is_circular_prime(89))
        self.assertTrue(is_circular_prime(1193))

if __name__ == '__main__':
    unittest.main()
