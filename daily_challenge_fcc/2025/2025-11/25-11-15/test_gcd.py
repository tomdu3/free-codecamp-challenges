import unittest
from gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_4_6(self):
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(6, 4), 2)

    def test_gcd_20_15(self):
        self.assertEqual(gcd(20, 15), 5)
        self.assertEqual(gcd(15, 20), 5)

    def test_gcd_13_17(self):
        self.assertEqual(gcd(13, 17), 1)
        self.assertEqual(gcd(17, 13), 1)

    def test_gcd_654_456(self):
        self.assertEqual(gcd(654, 456), 6)
        self.assertEqual(gcd(456, 654), 6)

    def test_gcd_3456_4320(self):
        self.assertEqual(gcd(3456, 4320), 864)
        self.assertEqual(gcd(4320, 3456), 864)

if __name__ == "__main__":
    unittest.main()