from unique_chars import all_unique
import unittest


class TestAllUnique(unittest.TestCase):
    def test_all_unique(self):
        self.assertEqual(all_unique("abc"), True)
        self.assertEqual(all_unique("aA"), True)
        self.assertEqual(all_unique("QwErTy123!@"), True)
        self.assertEqual(all_unique("~!@#$%^&*()_+"), True)
        self.assertEqual(all_unique("hello"), False)
        self.assertEqual(all_unique("freeCodeCamp"), False)
        self.assertEqual(all_unique("!@#*$%^&*()aA"), False)