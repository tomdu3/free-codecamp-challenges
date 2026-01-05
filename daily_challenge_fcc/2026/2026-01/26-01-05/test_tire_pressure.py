from tire_pressure import tire_status
import unittest


class TestTireStatus(unittest.TestCase):
    def test_tire_status(self):
        self.assertEqual(tire_status([32, 28, 35, 29], [2, 3]), ["Good", "Low", "Good", "Low"])
        self.assertEqual(tire_status([32, 28, 35, 30], [2, 2.3]), ["Good", "Low", "High", "Good"])
        self.assertEqual(tire_status([29, 26, 31, 28], [2.1, 2.5]), ["Low", "Low", "Good", "Low"])
        self.assertEqual(tire_status([31, 31, 30, 29], [1.5, 2]), ["High", "High", "High", "Good"])
        self.assertEqual(tire_status([30, 28, 30, 29], [1.9, 2.1]), ["Good", "Good", "Good", "Good"])

if __name__ == "__main__":
    unittest.main()
