from scaled_image import scaled_image
import unittest


class TestScaledImage(unittest.TestCase):
    def test_scale_image(self):
        self.assertEqual(scaled_image("800x600", 2), "1600x1200")
        self.assertEqual(scaled_image("100x100", 10), "1000x1000")
        self.assertEqual(scaled_image("1024x768", 0.5), "512x384")
        self.assertEqual(scaled_image("300x200", 1.5), "450x300")


if __name__ == "__main__":
    unittest.main()
