from zodiac_finder import get_sign
import unittest


class TestGetSign(unittest.TestCase):
    def test_get_sign(self):
        self.assertEqual(get_sign("2026-01-31"), "Aquarius")
        self.assertEqual(get_sign("2001-06-10"), "Gemini")
        self.assertEqual(get_sign("1985-09-07"), "Virgo")
        self.assertEqual(get_sign("2023-03-19"), "Pisces")
        self.assertEqual(get_sign("2045-11-05"), "Scorpio")
        self.assertEqual(get_sign("1985-12-06"), "Sagittarius")
        self.assertEqual(get_sign("2025-12-30"), "Capricorn")
        self.assertEqual(get_sign("2018-10-08"), "Libra")
        self.assertEqual(get_sign("1958-05-04"), "Taurus")


if __name__ == "__main__":
    unittest.main()