from consontant_count import has_consonant_count
import unittest


class TestConsonantCount(unittest.TestCase):
    def test_consonant_count(self):
        self.assertEqual(has_consonant_count("helloworld", 7), True)
        self.assertEqual(has_consonant_count("eieio", 5), False)
        self.assertEqual(has_consonant_count("freeCodeCamp Rocks!", 11), True)
        self.assertEqual(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24), False)
        self.assertEqual(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23), True)