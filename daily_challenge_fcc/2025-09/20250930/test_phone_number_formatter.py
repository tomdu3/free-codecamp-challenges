import unittest
from phone_number_formatter import format_number

class TestPhoneNumberFormatter(unittest.TestCase):
    def test_format_number_case1(self):
        self.assertEqual(format_number("05552340182"), "+0 (555) 234-0182")

    def test_format_number_case2(self):
        self.assertEqual(format_number("15554354792"), "+1 (555) 435-4792")

    def test_format_number_case3(self):
        self.assertEqual(format_number("25551234567"), "+2 (555) 123-4567")

    def test_format_number_case4(self):
        self.assertEqual(format_number("35559876543"), "+3 (555) 987-6543")

    def test_format_number_case5(self):
        self.assertEqual(format_number("45550000000"), "+4 (555) 000-0000")

    def test_format_number_case6(self):
        self.assertEqual(format_number("95559999999"), "+9 (555) 999-9999")


if __name__ == "__main__":
    unittest.main()