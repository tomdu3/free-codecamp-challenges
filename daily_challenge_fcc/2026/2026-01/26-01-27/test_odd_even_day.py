from odd_even_day import odd_or_even_day
import unittest


class TestOddOrEvenDay(unittest.TestCase):
    def test_odd_or_even_day(self):
        self.assertEqual(odd_or_even_day(1769472000000), "odd")
        self.assertEqual(odd_or_even_day(1769444440000), "even")
        self.assertEqual(odd_or_even_day(6739456780000), "odd")
        self.assertEqual(odd_or_even_day(1), "odd")
        self.assertEqual(odd_or_even_day(86400000), "even")
        self.assertEqual(odd_or_even_day(1769472000000.0), "odd")
        self.assertEqual(odd_or_even_day(1769444440000.0), "even")
        self.assertEqual(odd_or_even_day(6739456780000.0), "odd")
        self.assertEqual(odd_or_even_day(1.0), "odd")
        self.assertEqual(odd_or_even_day(86400000.0), "even")


if __name__ == "__main__":
    unittest.main()
