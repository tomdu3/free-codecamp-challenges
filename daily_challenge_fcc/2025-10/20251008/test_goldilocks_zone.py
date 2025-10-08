import unittest
from golidlocks_zone import goldilocks_zone

class TestGoldilocksZone(unittest.TestCase):

    def test_goldilocks_zone_1(self):
        self.assertAlmostEqual(goldilocks_zone(1)[0], 0.95, places=2)
        self.assertAlmostEqual(goldilocks_zone(1)[1], 1.37, places=2)

    def test_goldilocks_zone_0_5(self):
        self.assertAlmostEqual(goldilocks_zone(0.5)[0], 0.28, places=2)
        self.assertAlmostEqual(goldilocks_zone(0.5)[1], 0.41, places=2)

    def test_goldilocks_zone_6(self):
        self.assertAlmostEqual(goldilocks_zone(6)[0], 21.85, places=2)
        self.assertAlmostEqual(goldilocks_zone(6)[1], 31.51, places=2)

    def test_goldilocks_zone_3_7(self):
        self.assertAlmostEqual(goldilocks_zone(3.7)[0], 9.38, places=2)
        self.assertAlmostEqual(goldilocks_zone(3.7)[1], 13.52, places=2)

    def test_goldilocks_zone_20(self):
        self.assertAlmostEqual(goldilocks_zone(20)[0], 179.69, places=2)
        self.assertAlmostEqual(goldilocks_zone(20)[1], 259.13, places=2)

if __name__ == '__main__':
    unittest.main()
