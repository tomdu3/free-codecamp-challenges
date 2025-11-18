import unittest

from chars_100 import one_hundred

class TestOneHundred(unittest.TestCase):
    def test_one_hundred_string(self):
        self.assertEqual(one_hundred("One hundred "), "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ")
    
    def test_freeCodeCamp_string(self):
        self.assertEqual(one_hundred("freeCodeCamp "), "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC")
    
    def test_daily_challenges_string(self):
        self.assertEqual(one_hundred("daily challenges "), "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge")
    
    def test_exclamation_mark(self):
        self.assertEqual(one_hundred("!"), "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == '__main__':
    unittest.main()