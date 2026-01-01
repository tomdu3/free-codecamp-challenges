import unittest
from time_24_2_12 import to_12

class TestTo12(unittest.TestCase):
    def test_morning(self):
        self.assertEqual(to_12("1124"), "11:24 AM")
        self.assertEqual(to_12("0900"), "9:00 AM")
        self.assertEqual(to_12("0030"), "12:30 AM")
        self.assertEqual(to_12("0000"), "12:00 AM")
        self.assertEqual(to_12("0105"), "1:05 AM")

    def test_afternoon(self):
        self.assertEqual(to_12("1455"), "2:55 PM")
        self.assertEqual(to_12("1200"), "12:00 PM")
        self.assertEqual(to_12("1301"), "1:01 PM")
        self.assertEqual(to_12("1759"), "5:59 PM")

    def test_evening(self):
        self.assertEqual(to_12("2346"), "11:46 PM")
        self.assertEqual(to_12("2200"), "10:00 PM")
        self.assertEqual(to_12("2107"), "9:07 PM")

if __name__ == "__main__":
    unittest.main()