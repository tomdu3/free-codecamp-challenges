import unittest
from rectangle_count import count_rectangles

class TestCountRectangles(unittest.TestCase):
    def test_count_rectangles_case1(self):
        self.assertEqual(count_rectangles(1, 3), 6)

    def test_count_rectangles_case2(self):
        self.assertEqual(count_rectangles(3, 2), 18)

    def test_count_rectangles_case3(self):
        self.assertEqual(count_rectangles(1, 2), 3)

    def test_count_rectangles_case4(self):
        self.assertEqual(count_rectangles(5, 4), 150)

    def test_count_rectangles_case5(self):
        self.assertEqual(count_rectangles(11, 19), 12540)

if __name__ == "__main__":
    unittest.main()