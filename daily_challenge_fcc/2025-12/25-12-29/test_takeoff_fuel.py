from takeoff_fuel import fuel_to_add
import unittest


class TestFuelToAdd(unittest.TestCase):
    def test_fuel_to_add(self):
        self.assertEqual(fuel_to_add(0, 1), 1)
        self.assertEqual(fuel_to_add(5, 40), 6)
        self.assertEqual(fuel_to_add(10, 30), 0)
        self.assertEqual(fuel_to_add(896, 20500), 4520)
        self.assertEqual(fuel_to_add(1000, 50000), 12209)

if __name__ == '__main__':
    unittest.main()
