from symmetric_difference import difference
import unittest

class TestDifference(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(difference([1, 2, 3], [3, 4, 5]), [1, 2, 4, 5])

    def test_case_2(self):
        self.assertEqual(difference(["a", "b"], ["c", "b"]), ["a", "c"])

    def test_case_3(self):
        self.assertEqual(difference([1, "a", 2], [2, "b", "a"]), [1, "b"])

    def test_case_4(self):
        self.assertEqual(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 4, 6, 8])
