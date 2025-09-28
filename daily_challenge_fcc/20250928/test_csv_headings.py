import unittest
from csv_headings import get_headings

class TestGetHeadings(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_headings("name,age,city"), ["name", "age", "city"])

    def test_spaces(self):
        self.assertEqual(get_headings("first name,last name,phone"), ["first name", "last name", "phone"])
        self.assertEqual(get_headings("username , email , signup date "), ["username", "email", "signup date"])

    def test_empty_string(self):
        self.assertEqual(get_headings(""), [""])

    def test_single_heading(self):
        self.assertEqual(get_headings("id"), ["id"])

    def test_trailing_comma(self):
        self.assertEqual(get_headings("name,age,"), ["name", "age", ""])

    def test_leading_comma(self):
        self.assertEqual(get_headings(",name,age"), ["", "name", "age"])

    def test_multiple_commas(self):
        self.assertEqual(get_headings("a,,b"), ["a", "", "b"])

    def test_spaces_only(self):
        self.assertEqual(get_headings("  ,  , "), ["", "", ""])

if __name__ == "__main__":
    unittest.main()