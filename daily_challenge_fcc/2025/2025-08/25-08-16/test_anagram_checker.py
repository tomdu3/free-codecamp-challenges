import unittest
from anagram_checker import are_anagrams

class TestAnagramChecker(unittest.TestCase):
    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("School master", "The classroom"))
        self.assertTrue(are_anagrams("A gentleman", "Elegant man"))
        self.assertFalse(are_anagrams("Hello", "World"))
        self.assertFalse(are_anagrams("apple", "banana"))
        self.assertFalse(are_anagrams("cat", "dog"))
