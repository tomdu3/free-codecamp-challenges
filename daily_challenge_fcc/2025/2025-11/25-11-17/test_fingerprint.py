import unittest
from fingerprint import is_match

class TestFingerprint(unittest.TestCase):
    def test_identical_simple(self):
        self.assertTrue(is_match("helloworld", "helloworld"))

    def test_b_extra_char(self):
        self.assertFalse(is_match("helloworld", "helloworlds"))

    def test_first_char_diff(self):
        self.assertTrue(is_match("helloworld", "jelloworld"))

    def test_long_identical(self):
        s = "thequickbrownfoxjumpsoverthelazydog"
        self.assertTrue(is_match(s, s))

    def test_similar_but_different(self):
        a = "theslickbrownfoxjumpsoverthelazydog"
        b = "thequickbrownfoxjumpsoverthehazydog"
        self.assertTrue(is_match(a, b))

    def test_different_end(self):
        a = "thequickbrownfoxjumpsoverthelazydog"
        b = "thequickbrownfoxjumpsoverthehazycat"
        self.assertFalse(is_match(a, b))

if __name__ == "__main__":
    unittest.main()