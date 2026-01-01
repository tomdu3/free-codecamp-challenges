from roman_num import to_roman
import unittest


class TestRomanNum(unittest.TestCase):
    def test_roman_num(self):
        self.assertEqual(to_roman(18), "XVIII")
        self.assertEqual(to_roman(19), "XIX")
        self.assertEqual(to_roman(1464), "MCDLXIV")
        self.assertEqual(to_roman(2025), "MMXXV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
