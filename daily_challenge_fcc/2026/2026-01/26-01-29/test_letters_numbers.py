from letters_numbers import separate_letters_and_numbers
import unittest

"""
Tests
Waiting:1. separate_letters_and_numbers("ABC123") should return "ABC-123".
Waiting:2. separate_letters_and_numbers("Route66") should return "Route-66.
Waiting:3. separate_letters_and_numbers("H3LL0W0RLD") should return "H-3-LL-0-W-0-RLD".
Waiting:4. separate_letters_and_numbers("a1b2c3d4") should return "a-1-b-2-c-3-d-4".
"""

class TestSeparateLettersAndNumbers(unittest.TestCase):
    def test_separate_letters_and_numbers(self):
        self.assertEqual(separate_letters_and_numbers("ABC123"), "ABC-123")
        self.assertEqual(separate_letters_and_numbers("Route66"), "Route-66")
        self.assertEqual(separate_letters_and_numbers("H3LL0W0RLD"), "H-3-LL-0-W-0-RLD")
        self.assertEqual(separate_letters_and_numbers("a1b2c3d4"), "a-1-b-2-c-3-d-4")


if __name__ == "__main__":
    unittest.main()
