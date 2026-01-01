import unittest
from miles_kms import convert_to_km
from math import isclose
import sys
sys.path.append("..")
sys.path.append(".")

class TestMilesToKm(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert_to_km(1), 1.61)

    def test_2(self):
        self.assertEqual(convert_to_km(21), 33.8)

    def test_3(self):
        self.assertEqual(convert_to_km(3.5), 5.63)

    def test_4(self):
        self.assertEqual(convert_to_km(0), 0)

    def test_5(self):
        self.assertEqual(convert_to_km(0.621371), 1)

