import unittest
from longest_word import get_longest_word

class TestGetLongestWord(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_longest_word("coding is fun"), "coding")
    
    def test_with_punctuation(self):
        self.assertEqual(get_longest_word("Coding challenges are fun and educational."), "educational")
    
    def test_multiple_long_words(self):
        self.assertEqual(get_longest_word("This sentence has multiple long words."), "sentence")
    
    def test_single_word(self):
        self.assertEqual(get_longest_word("hello"), "hello")
    
    def test_all_same_length(self):
        self.assertEqual(get_longest_word("cat dog bat"), "cat")
    
    def test_multiple_punctuation(self):
        self.assertEqual(get_longest_word("Wow! Amazing, incredible."), "incredible")
    
    def test_numbers_and_words(self):
        self.assertEqual(get_longest_word("abc 12345 xyz"), "12345")
    
    def test_hyphenated_word(self):
        self.assertEqual(get_longest_word("well-known fact"), "well-known")
    
    def test_multiple_sentences(self):
        self.assertEqual(get_longest_word("First sentence. Second sentence is longer."), "sentence")

if __name__ == "__main__":
    unittest.main()