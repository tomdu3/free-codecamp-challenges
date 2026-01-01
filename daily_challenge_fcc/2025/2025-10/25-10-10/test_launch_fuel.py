import unittest
from launch_fuel import launch_fuel

class TestLaunchFuel(unittest.TestCase):
    def test_50(self):
        self.assertEqual(launch_fuel(50), 12.4)

    def test_500(self):
        self.assertEqual(launch_fuel(500), 124.8)

    def test_243(self):
        self.assertEqual(launch_fuel(243), 60.7)

    def test_11000(self):
        self.assertEqual(launch_fuel(11000), 2749.8)

    def test_6214(self):
        self.assertEqual(launch_fuel(6214), 1553.4)

    def test_zero_payload(self):
        self.assertEqual(launch_fuel(0), 0.0)

    def test_small_payload(self):
        self.assertEqual(launch_fuel(1), 0.2)

if __name__ == "__main__":
    unittest.main()