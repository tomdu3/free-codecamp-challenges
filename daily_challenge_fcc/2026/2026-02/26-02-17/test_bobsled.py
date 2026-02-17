from bobsled import check_eligibility
import unittest


class TestBobsled(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_eligibility([78], 165), "Eligible")

    def test_2(self):
        self.assertEqual(check_eligibility([80], 160), "Not Eligible")

    def test_3(self):
        self.assertEqual(check_eligibility([80], 170), "Not Eligible")

    def test_4(self):
        self.assertEqual(check_eligibility([85, 90], 170), "Eligible")

    def test_5(self):
        self.assertEqual(check_eligibility([85, 95], 168), "Not Eligible")

    def test_6(self):
        self.assertEqual(check_eligibility([112, 97], 185), "Not Eligible")

    def test_7(self):
        self.assertEqual(check_eligibility([110, 102, 90, 106], 222), "Eligible")

    def test_8(self):
        self.assertEqual(check_eligibility([106, 99, 90, 88], 205), "Not Eligible")

    def test_9(self):
        self.assertEqual(check_eligibility([106, 99, 103, 96], 227), "Not Eligible")


if __name__ == "__main__":
    unittest.main()
