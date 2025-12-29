from array_diff import array_diff
import unittest

class TestArrayDiff(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]), ["cherry"])
        self.assertEqual(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]), ["cherry"])
        self.assertEqual(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]), ["eight", "four", "six", "two"])
        self.assertEqual(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]), ["five", "one", "seven", "three"])
        self.assertEqual(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]), ["freeCodeCamp", "rocks"])

if __name__ == "__main__":
    unittest.main()
