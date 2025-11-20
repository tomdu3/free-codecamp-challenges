import unittest
from longest_word import longest_word

class TestLongestWord(unittest.TestCase):
    def test_quick_red_fox(self):
        self.assertEqual(longest_word("The quick red fox"), "quick")

    def test_hello_coding_challenge(self):
        self.assertEqual(longest_word("Hello coding challenge."), "challenge")

    def test_do_try_this_at_home(self):
        self.assertEqual(longest_word("Do Try This At Home."), "This")

    def test_sentence_with_punctuation(self):
        self.assertEqual(longest_word("This sentence... has commas, ellipses, and an exlamation point!"), "exlamation")

    def test_a_tie_no_way(self):
        self.assertEqual(longest_word("A tie? No way!"), "tie")

    def test_wouldnt_you_like_to_know(self):
        self.assertEqual(longest_word("Wouldn't you like to know."), "Wouldnt")

if __name__ == '__main__':
    unittest.main()
