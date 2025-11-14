import unittest
from weekend import days_until_weekend

class Tests(unittest.TestCase):
    def test_2025_11_14(self):
        self.assertEqual(days_until_weekend("2025-11-14"), "1 day until the weekend.")

    def test_2025_01_01(self):
        self.assertEqual(days_until_weekend("2025-01-01"), "3 days until the weekend.")

    def test_2025_12_06_weekend(self):
        self.assertEqual(days_until_weekend("2025-12-06"), "It's the weekend!")

    def test_2026_01_27(self):
        self.assertEqual(days_until_weekend("2026-01-27"), "4 days until the weekend.")

    def test_2026_09_07(self):
        self.assertEqual(days_until_weekend("2026-09-07"), "5 days until the weekend.")

    def test_2026_11_29_weekend(self):
        self.assertEqual(days_until_weekend("2026-11-29"), "It's the weekend!")

if __name__ == "__main__":
    unittest.main()