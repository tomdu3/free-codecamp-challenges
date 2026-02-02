from groundhog_day import groundhog_day_prediction
import unittest


class TestGroundhogDayPrediction(unittest.TestCase):
    def test_groundhog_day_prediction(self):
        self.assertEqual(groundhog_day_prediction(True), "Looks like we'll have six more weeks of winter.")
        self.assertEqual(groundhog_day_prediction(False), "It's going to be an early spring.")
        self.assertEqual(groundhog_day_prediction(None), "No prediction this year.")
        self.assertEqual(groundhog_day_prediction(" "), "No prediction this year.")
        self.assertEqual(groundhog_day_prediction("True"), "No prediction this year.")

if __name__ == "__main__":
    unittest.main()