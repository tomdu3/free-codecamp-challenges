from date_convert import format_date

import unittest

class TestFormatDate(unittest.TestCase):
    def test_december_6_2025(self):
        self.assertEqual(format_date("December 6, 2025"), "2025-12-06")

    def test_january_1_2000(self):
        self.assertEqual(format_date("January 1, 2000"), "2000-01-01")

    def test_november_11_1111(self):
        self.assertEqual(format_date("November 11, 1111"), "1111-11-11")

    def test_september_7_512(self):
        self.assertEqual(format_date("September 7, 512"), "512-09-07")

    def test_may_4_1950(self):
        self.assertEqual(format_date("May 4, 1950"), "1950-05-04")

    def test_february_29_1992(self):
        self.assertEqual(format_date("February 29, 1992"), "1992-02-29")

if __name__ == '__main__':
    unittest.main()
