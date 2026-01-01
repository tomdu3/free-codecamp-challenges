from md_bq_parser import parse_blockquote
import unittest


class TestMdBqParser(unittest.TestCase):
    def test_md_bq_parser(self):
        self.assertEqual(parse_blockquote("> This is a quote"), "<blockquote>This is a quote</blockquote>")
        self.assertEqual(parse_blockquote(" > This is also a quote"), "<blockquote>This is also a quote</blockquote>")
        self.assertEqual(parse_blockquote(" > So Is This"), "<blockquote>So Is This</blockquote>")
        self.assertEqual(parse_blockquote(" <> This is not a quote"), "")
        self.assertEqual(parse_blockquote("This is not a quote"), "")
        self.assertEqual(parse_blockquote(""), "")
