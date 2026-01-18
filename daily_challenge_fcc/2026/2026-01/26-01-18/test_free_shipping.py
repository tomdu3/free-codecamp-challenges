from free_shipping import gets_free_shipping
import unittest

class TestFreeShipping(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gets_free_shipping(["shoes"], 50), True)
    def test_2(self):
        self.assertEqual(gets_free_shipping(["hat", "socks"], 50), False)
    def test_3(self):
        self.assertEqual(gets_free_shipping(["jeans", "shirt", "jacket"], 75), True)
    def test_4(self):
        self.assertEqual(gets_free_shipping(["socks", "socks", "hat"], 75), False)
    def test_5(self):
        self.assertEqual(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100), True)
    def test_6(self):
        self.assertEqual(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200), False)

if __name__ == "__main__":
    unittest.main()
