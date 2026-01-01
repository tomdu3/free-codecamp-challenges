from md_ol_converter import convert_list_item
import unittest

class TestMdOlConverter(unittest.TestCase):
    def test_convert_list_item_valid_simple(self):
        self.assertEqual(convert_list_item("1. My item"), "<li>My item</li>")

    def test_convert_list_item_valid_with_leading_space(self):
        self.assertEqual(convert_list_item(" 1.  Another item"), "<li>Another item</li>")

    def test_convert_list_item_invalid_period_space(self):
        self.assertEqual(convert_list_item("1 . invalid item"), "Invalid format")

    def test_convert_list_item_valid_different_number(self):
        self.assertEqual(convert_list_item("2. list item text"), "<li>list item text</li>")

    def test_convert_list_item_invalid_leading_period(self):
        self.assertEqual(convert_list_item(". invalid again"), "Invalid format")

    def test_convert_list_item_invalid_leading_letter(self):
        self.assertEqual(convert_list_item("A. last invalid"), "Invalid format")
