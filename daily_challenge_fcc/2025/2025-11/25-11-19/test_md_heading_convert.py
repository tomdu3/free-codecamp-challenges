import unittest
from md_heading_convert import convert

class TestMdHeadingConvert(unittest.TestCase):

    def test_level_1_heading(self):
        self.assertEqual(convert("# My level 1 heading"), "<h1>My level 1 heading</h1>")

    def test_invalid_format_no_hash(self):
        self.assertEqual(convert("My heading"), "Invalid format")

    def test_level_5_heading(self):
        self.assertEqual(convert("##### My level 5 heading"), "<h5>My level 5 heading</h5>")

    def test_invalid_format_no_space_after_hash(self):
        self.assertEqual(convert("#My heading"), "Invalid format")

    def test_level_3_heading_with_leading_trailing_spaces(self):
        self.assertEqual(convert("  ###  My level 3 heading"), "<h3>My level 3 heading</h3>")

    def test_invalid_format_level_7_heading(self):
        self.assertEqual(convert("####### My level 7 heading"), "Invalid format")

    def test_level_2_heading_with_hash_in_text(self):
        self.assertEqual(convert("## My #2 heading"), "<h2>My #2 heading</h2>")

if __name__ == '__main__':
    unittest.main()
