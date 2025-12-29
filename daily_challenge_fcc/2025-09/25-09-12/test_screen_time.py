from screen_time import too_much_screen_time
import unittest



class TestScreenTime(unittest.TestCase):
    def test_screen_time(self):
        self.assertEqual(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]), False)
        self.assertEqual(too_much_screen_time([7, 8, 8, 4, 2, 2, 3]), False)
        self.assertEqual(too_much_screen_time([5, 6, 6, 6, 6, 6, 6]), False)
        self.assertEqual(too_much_screen_time([1, 2, 3, 11, 1, 3, 4]), True)
        self.assertEqual(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]), True)
        self.assertEqual(too_much_screen_time([3, 3, 5, 8, 8, 9, 4]), True)
        self.assertEqual(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]), True)


if __name__ == '__main__':
    unittest.main()
