from daily_hours import daylight_hours
import unittest

"""
Tests
Waiting:1. daylight_hours(45) should return 9.
Waiting:2. daylight_hours(0) should return 12.
Waiting:3. daylight_hours(-90) should return 24.
Waiting:4. daylight_hours(-10) should return 12.
Waiting:5. daylight_hours(23) should return 10.
Waiting:6. daylight_hours(88) should return 0.
Waiting:7. daylight_hours(-33) should return 13.
Waiting:8. daylight_hours(70) should return 2.
"""

class TestDaylightHours(unittest.TestCase):
    def test_daylight_hours(self):
        self.assertEqual(daylight_hours(45), 9)
        self.assertEqual(daylight_hours(0), 12)
        self.assertEqual(daylight_hours(-90), 24)
        self.assertEqual(daylight_hours(-10), 12)
        self.assertEqual(daylight_hours(23), 10)
        self.assertEqual(daylight_hours(88), 0)
        self.assertEqual(daylight_hours(-33), 13)
        self.assertEqual(daylight_hours(70), 2)
    
