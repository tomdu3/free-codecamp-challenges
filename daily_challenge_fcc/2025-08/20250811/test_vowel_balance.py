import unittest
from vowel_balance import is_balanced

class TestVowelBalance(unittest.TestCase):
    def test_racecar(self):
        self.assertTrue(is_balanced("racecar"))

    def test_lorem_ipsum(self):
        self.assertTrue(is_balanced("Lorem Ipsum"))

    def test_kitty_ipsum(self):
        self.assertFalse(is_balanced("Kitty Ipsum"))

    def test_string(self):
        self.assertFalse(is_balanced("string"))

    def test_single_space(self):
        self.assertTrue(is_balanced(" "))

    def test_alphabet(self):
        self.assertFalse(is_balanced("abcdefghijklmnopqrstuvwxyz"))

    def test_special_characters(self):
        self.assertTrue(is_balanced("123A#b!E&*456-o.U"))

    # Additional tests
    def test_empty_string(self):
        self.assertTrue(is_balanced(""))

    def test_single_vowel(self):
        self.assertTrue(is_balanced("a"))

    def test_two_vowels(self):
        self.assertTrue(is_balanced("ae"))

    def test_no_vowels(self):
        self.assertTrue(is_balanced("bcdfg"))

    def test_all_vowels(self):
        self.assertTrue(is_balanced("aeiouAEIOU"))

    def test_odd_length_unbalanced(self):
        self.assertTrue(is_balanced("abcdefg"))

if __name__ == "__main__":
    unittest.main()