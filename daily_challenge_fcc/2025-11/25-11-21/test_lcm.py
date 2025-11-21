import unittest

from lcm import lcm

class TestLCM(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(9, 6), 18)
        self.assertEqual(lcm(10, 100), 100)
        self.assertEqual(lcm(13, 17), 221)
        self.assertEqual(lcm(45, 70), 630)

if __name__ == '__main__':
    unittest.main()