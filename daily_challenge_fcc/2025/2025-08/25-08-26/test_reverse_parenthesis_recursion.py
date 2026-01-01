from reverse_parenthesis_recursion import decode
import unittest

"""
Tests

Waiting: 1. decode("(f(b(dc)e)a)") should return "abcdef".
Waiting: 2. decode("((is?)(a(t d)h)e(n y( uo)r)aC)") should return "Can you read this?".
Waiting: 3. decode("f(Ce(re))o((e(aC)m)d)p") should return "freeCodeCamp".
"""

class TestReverseParenthesis(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(decode("(f(b(dc)e)a)") , "abcdef")
        self.assertEqual(decode("((is?)(a(t d)h)e(n y( uo)r)aC)") , "Can you read this?")
        self.assertEqual(decode("f(Ce(re))o((e(aC)m)d)p") , "freeCodeCamp")

if __name__ == "__main__":
    unittest.main()
    