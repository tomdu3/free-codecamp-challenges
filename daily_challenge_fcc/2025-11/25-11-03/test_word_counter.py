import unittest
from word_counter import count_words

class TestWordCounter(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(count_words("Hello world"), 2)

    def test_long_sentence(self):
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog."), 9)

    def test_coding_challenges(self):
        self.assertEqual(count_words("I like coding challenges!"), 4)

    def test_javascript_and_python(self):
        self.assertEqual(count_words("Complete the challenge in JavaScript and Python."), 7)

    def test_missing_semicolon(self):
        self.assertEqual(count_words("The missing semi-colon crashed the entire internet."), 7)

if __name__ == '__main__':
    unittest.main()
