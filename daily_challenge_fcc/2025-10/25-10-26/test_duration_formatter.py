import unittest
from duration_formatter import format

class TestDurationFormatter(unittest.TestCase):
    def test_format_minutes_seconds(self):
        self.assertEqual(format(500), "8:20")
        self.assertEqual(format(1), "0:01")
    
    def test_format_hours_minutes_seconds(self):
        self.assertEqual(format(4000), "1:06:40")
        self.assertEqual(format(5555), "1:32:35")
        self.assertEqual(format(99999), "27:46:39")

if __name__ == '__main__':
    unittest.main()