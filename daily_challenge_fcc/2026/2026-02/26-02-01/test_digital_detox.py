from digital_detox import digital_detox
import unittest


class TestDigitalDetox(unittest.TestCase):
    def test_digital_detox(self):
        self.assertEqual(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]), True)
        self.assertEqual(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]), False)
        self.assertEqual(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]), True)
        self.assertEqual(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]), False)
        self.assertEqual(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]), True)
        self.assertEqual(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]), False)

if __name__ == "__main__":
    unittest.main()