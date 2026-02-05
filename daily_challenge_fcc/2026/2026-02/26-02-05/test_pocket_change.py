from pocket_change import count_change
import unittest



class TestPocketChange(unittest.TestCase):
    def test_count_change(self):
        self.assertEqual(count_change([25, 10, 5, 1]), "$0.41")
        self.assertEqual(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]), "$1.43")
        self.assertEqual(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]), "$37.55")
        self.assertEqual(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]), "$0.70")
        self.assertEqual(count_change([1]), "$0.01")
        self.assertEqual(count_change([25, 25, 25, 25]), "$1.00")

if __name__ == '__main__':
    unittest.main()
