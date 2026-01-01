from md_i_parser import parse_italics
import unittest

"""
Tests

Waiting: 1. parse_italics("*This is italic*") should return "<i>This is italic</i>".
Waiting: 2. parse_italics("_This is also italic_") should return "<i>This is also italic</i>".
Waiting: 3. parse_italics("*This is not italic *") should return "*This is not italic *".
Waiting: 4. parse_italics("_ This is also not italic_") should return "_ This is also not italic_".
Waiting: 5. parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.") should return "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.".
"""

class TestMdIParser(unittest.TestCase):
    def test_parse_italics(self):
        self.assertEqual(parse_italics("*This is italic*"), "<i>This is italic</i>")
        self.assertEqual(parse_italics("_This is also italic_"), "<i>This is also italic</i>")
        self.assertEqual(parse_italics("*This is not italic *"), "*This is not italic *")
        self.assertEqual(parse_italics("_ This is also not italic_"), "_ This is also not italic_")
        self.assertEqual(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."), "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.")


if __name__ == '__main__':
    unittest.main()
