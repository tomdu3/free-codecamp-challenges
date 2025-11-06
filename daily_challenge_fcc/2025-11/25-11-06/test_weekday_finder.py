import unittest
from weekday_finder import get_weekday


class TestWeekdayFinder(unittest.TestCase):
    def test_weekday_finder(self):
        self.assertEqual(get_weekday("2025-11-06"), "Thursday")
        self.assertEqual(get_weekday("1999-12-31"), "Friday")
        self.assertEqual(get_weekday("1111-11-11"), "Saturday")
        self.assertEqual(get_weekday("2112-12-21"), "Wednesday")
        self.assertEqual(get_weekday("2345-10-01"), "Monday")
