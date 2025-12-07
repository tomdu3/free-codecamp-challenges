from string_compression import compress_string
import unittest

class TestStringCompression(unittest.TestCase):
    def test_compress_string_basic_repetition(self):
        self.assertEqual(compress_string("yes yes yes please"), "yes(3) please")

    def test_compress_string_middle_repetition(self):
        self.assertEqual(compress_string("I have have have apples"), "I have(3) apples")

    def test_compress_string_multiple_repetitions(self):
        self.assertEqual(compress_string("one one three and to the the the the"), "one(2) three and to the(4)")

    def test_compress_string_all_repetitions(self):
        self.assertEqual(compress_string("route route route route route route tee tee tee tee tee tee"), "route(6) tee(6)")

if __name__ == '__main__':
    unittest.main()
