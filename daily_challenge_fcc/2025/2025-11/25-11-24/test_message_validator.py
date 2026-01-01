import unittest
from message_validator import is_valid_message

class TestMessageValidator(unittest.TestCase):
    def test_hello_world(self):
        self.assertTrue(is_valid_message("hello world", "hw"))

    def test_all_caps(self):
        self.assertTrue(is_valid_message("ALL CAPITAL LETTERS", "acl"))

    def test_coding_challenge_boring_false(self):
        self.assertFalse(is_valid_message("Coding challenge are boring.", "cca"))

    def test_quick_brown_fox_long_true(self):
        self.assertTrue(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))

    def test_quick_brown_fox_long_false(self):
        self.assertFalse(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))

if __name__ == '__main__':
    unittest.main()
