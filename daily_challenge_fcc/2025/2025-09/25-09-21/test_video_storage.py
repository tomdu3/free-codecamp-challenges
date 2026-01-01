import unittest
from video_storage import number_of_videos

class TestNumberOfVideos(unittest.TestCase):
    def test_valid_gb_mb(self):
        self.assertEqual(number_of_videos(500, "MB", 100, "GB"), 200)

    def test_invalid_video_unit(self):
        self.assertEqual(number_of_videos(2000, "TB", 1, "TB"), "Invalid video unit")

    def test_invalid_drive_unit(self):
        self.assertEqual(number_of_videos(2000, "MB", 100000, "MB"), "Invalid drive unit")

    def test_valid_kb_tb(self):
        self.assertEqual(number_of_videos(500000, "KB", 2, "TB"), 4000)

    def test_valid_float_gb_tb(self):
        self.assertEqual(number_of_videos(1.5, "GB", 2.2, "TB"), 1466)

if __name__ == "__main__":
    unittest.main()