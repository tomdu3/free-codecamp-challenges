import unittest
from vowel_consonants import count


class TestVowelsConsonants(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count("Hello World"), [3, 7])
        self.assertEqual(count("JavaScript"), [3, 7])
        self.assertEqual(count("Python"), [1, 5])
        self.assertEqual(count("freeCodeCamp"), [5, 7])
        self.assertEqual(count("Hello, World!"), [3, 7])
        self.assertEqual(
            count("The quick brown fox jumps over the lazy dog."), [11, 24]
        )
