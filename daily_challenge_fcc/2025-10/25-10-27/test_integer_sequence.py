import unittest
from integer_sequence import sequence

class TestSequence(unittest.TestCase):
    def test_sequence_5(self):
        self.assertEqual(sequence(5), "12345")

    def test_sequence_10(self):
        self.assertEqual(sequence(10), "12345678910")

    def test_sequence_1(self):
        self.assertEqual(sequence(1), "1")

    def test_sequence_27(self):
        self.assertEqual(
            sequence(27),
            "123456789101112131415161718192021222324252627"
        )

if __name__ == "__main__":
    unittest.main()