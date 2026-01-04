from leap import is_leap_year
import unittest


class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(2100))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1999))
        self.assertTrue(is_leap_year(2040))
        self.assertFalse(is_leap_year(2026))

if __name__ == '__main__':
    unittest.main()

