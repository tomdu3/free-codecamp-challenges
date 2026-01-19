from energy_consumption import compare_energy
import unittest


class TestEnergyConsumption(unittest.TestCase):
    def test_workout(self):
        self.assertEqual(compare_energy(250, 50), "Workout")

    def test_devices(self):
        self.assertEqual(compare_energy(100, 200), "Devices")

    def test_equal(self):
        self.assertEqual(compare_energy(450, 523), "Equal")

    def test_workout2(self):
        self.assertEqual(compare_energy(300, 75), "Workout")

    def test_devices2(self):
        self.assertEqual(compare_energy(200, 250), "Devices")

    def test_equal2(self):
        self.assertEqual(compare_energy(900, 1046), "Equal")

if __name__ == '__main__':
    unittest.main()
