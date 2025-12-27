from mile_pace import mile_pace
import unittest

"""
Tests

Waiting: 1. mile_pace(3, "24:00") should return "08:00".
Waiting: 2. mile_pace(1, "06:45") should return "06:45".
Waiting: 3. mile_pace(2, "07:00") should return "03:30".
Waiting: 4. mile_pace(26.2, "120:35") should return "04:36".
"""

class TestMilePace(unittest.TestCase):
    def test_mile_pace(self):
        self.assertEqual(mile_pace(3, "24:00"), "08:00")
        self.assertEqual(mile_pace(1, "06:45"), "06:45")
        self.assertEqual(mile_pace(2, "07:00"), "03:30")
        self.assertEqual(mile_pace(26.2, "120:35"), "04:36")
