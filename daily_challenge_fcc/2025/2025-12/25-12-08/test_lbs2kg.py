from lbs2kg import convert_lbs_to_kg
import unittest

class TestLbsToKg(unittest.TestCase):
    def test_one_pound(self):
        self.assertEqual(convert_lbs_to_kg(1), "1 pound equals 0.45 kilograms.")

    def test_zero_pounds(self):
        self.assertEqual(convert_lbs_to_kg(0), "0 pounds equals 0.00 kilograms.")

    def test_hundred_pounds(self):
        self.assertEqual(convert_lbs_to_kg(100), "100 pounds equals 45.36 kilograms.")

    def test_two_point_five_pounds(self):
        self.assertEqual(convert_lbs_to_kg(2.5), "2.5 pounds equals 1.13 kilograms.")

    def test_one_kg_equivalent(self):
        self.assertEqual(convert_lbs_to_kg(2.20462), "2.20462 pounds equals 1.00 kilogram.")



