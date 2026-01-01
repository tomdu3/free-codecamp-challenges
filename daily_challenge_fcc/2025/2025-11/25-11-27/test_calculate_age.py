import unittest
from calculate_age import calculate_age

class TestCalculateAge(unittest.TestCase):
    def test_age_calculation_1(self):

        self.assertEqual(calculate_age("2000-11-20"), 25)
    
    def test_age_calculation_2(self):
        self.assertEqual(calculate_age("2000-12-01"), 24)

    def test_age_calculation_3(self):
        self.assertEqual(calculate_age("2014-10-25"), 11)

    def test_age_calculation_4(self):
        self.assertEqual(calculate_age("1994-01-06"), 31)

    def test_age_calculation_5(self):
        self.assertEqual(calculate_age("1994-12-14"), 30)

if __name__ == '__main__':
    unittest.main()
