from truncate_text import truncate_text
import unittest


class TestTruncateText(unittest.TestCase):

    def test_non_truncated(self):
        self.assertEqual(truncate_text("Hello, world!"), "Hello, world!")
        self.assertEqual(truncate_text("Exactly twenty chars"), "Exactly twenty chars")

    def test_truncated(self):
        self.assertEqual(truncate_text("This string should get truncated."), "This string shoul...")
        self.assertEqual(truncate_text("....................."), "....................")


if __name__ == "__main__":
    unittest.main()
