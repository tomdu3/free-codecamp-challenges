import unittest
from letters_digits import digits_or_letters

class Tests(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(digits_or_letters("abc123"), "tie")
        self.assertEqual(digits_or_letters("P455W0RD"), "tie")
        self.assertEqual(digits_or_letters("a1b2c3"), "tie")
        self.assertEqual(digits_or_letters("A1B2C3"), "tie")
        self.assertEqual(digits_or_letters(""), "tie")  # 0 letters, 0 digits

    def test_letters(self):
        self.assertEqual(digits_or_letters("a1b2c3d"), "letters")
        self.assertEqual(digits_or_letters("abc123!@#DEF"), "letters")
        self.assertEqual(digits_or_letters("abcdef"), "letters")
        self.assertEqual(digits_or_letters("abc123def"), "letters")
        self.assertEqual(digits_or_letters("A!B@C#1"), "letters")

    def test_digits(self):
        self.assertEqual(digits_or_letters("1a2b3c4"), "digits")
        self.assertEqual(digits_or_letters("H3110 W0R1D"), "digits")
        self.assertEqual(digits_or_letters("123456"), "digits")
        self.assertEqual(digits_or_letters("1a2b3c4d5e6f7g8h9i0"), "digits")
        self.assertEqual(digits_or_letters("123abc456def789"), "digits")

if __name__ == "__main__":
    unittest.main()