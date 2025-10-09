import unittest
from moon_phase import moon_phase

class TestMoonPhase(unittest.TestCase):
    def test_new_phase(self):
        self.assertEqual(moon_phase("2000-01-12"), "New")
        self.assertEqual(moon_phase("2022-12-14"), "New")
        self.assertEqual(moon_phase("2000-01-06"), "New")

    
    def test_waxing_phase(self):
        self.assertEqual(moon_phase("2000-01-13"), "Waxing")
    
    def test_full_phase(self):
        self.assertEqual(moon_phase("2014-10-15"), "Full")
    
    def test_waning_phase(self):
        self.assertEqual(moon_phase("2012-10-21"), "Waning")


if __name__ == "__main__":
    unittest.main()