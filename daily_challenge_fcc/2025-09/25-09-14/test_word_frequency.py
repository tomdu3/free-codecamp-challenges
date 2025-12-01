import unittest
from word_frequency import get_words

class TestWordFrequency(unittest.TestCase):

    def test_get_words_1(self):
        self.assertEqual(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"), ["coding", "python", "in"])

    def test_get_words_2(self):
        self.assertEqual(get_words("I like coding. I like testing. I love debugging!"), ["i", "like", "coding"])

    def test_get_words_3(self):
        self.assertEqual(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"), ["debug", "test", "deploy"])

if __name__ == '__main__':
    unittest.main()
