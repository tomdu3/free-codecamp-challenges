from speed_check import speed_check
import unittest


class TestSpeedCheck(unittest.TestCase):
    def test_speed_check(self):
        self.assertEqual(speed_check(30, 70), "Not Speeding")
        self.assertEqual(speed_check(40, 60), "Warning")
        self.assertEqual(speed_check(40, 65), "Not Speeding")
        self.assertEqual(speed_check(60, 90), "Ticket")
        self.assertEqual(speed_check(65, 100), "Warning")
        self.assertEqual(speed_check(88, 40), "Ticket")

if __name__ == "__main__":
    unittest.main()
