import unittest
from spam_detector import is_spam

class TestSpamDetector(unittest.TestCase):
    def test_valid_number(self):
        self.assertFalse(is_spam("+0 (200) 234-0182"))
        self.assertFalse(is_spam("+00 (555) 234-0182"))

    def test_invalid_country_code(self):
        self.assertTrue(is_spam("+091 (555) 309-1922"))
        self.assertTrue(is_spam("+1 (555) 435-4792"))

    def test_invalid_area_code(self):
        self.assertTrue(is_spam("+0 (955) 234-4364"))
        self.assertTrue(is_spam("+0 (155) 131-6943"))

    def test_local_number_sum_in_second_part(self):
        self.assertTrue(is_spam("+0 (555) 135-0192"))
        self.assertTrue(is_spam("+0 (555) 564-1987"))

    def test_repeated_digits(self):
        self.assertTrue(is_spam("+0 (222) 222-2222"))  # repeated digits in all parts
        self.assertTrue(is_spam("+0 (555) 555-5555"))  # repeated digits in all parts

    def test_edge_area_code(self):
        self.assertFalse(is_spam("+0 (200) 123-4567"))  # lower bound
        self.assertFalse(is_spam("+0 (900) 123-4567"))  # upper bound
        self.assertTrue(is_spam("+0 (199) 123-4567"))   # below lower bound
        self.assertTrue(is_spam("+0 (901) 123-4567"))   # above upper bound

    def test_country_code_length(self):
        self.assertTrue(is_spam("+000 (555) 234-0182"))  # country code too long


if __name__ == "__main__":
    unittest.main()