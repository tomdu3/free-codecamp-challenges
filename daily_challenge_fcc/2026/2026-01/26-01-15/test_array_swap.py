from array_swap import array_swap
import unittest


class TestArraySwap(unittest.TestCase):
    def test_array_swap(self):
        self.assertEqual(array_swap(["A", "B"]), ["B", "A"])
        self.assertEqual(array_swap([25, 20]), [20, 25])
        self.assertEqual(array_swap([True, False]), [False, True])
        self.assertEqual(array_swap(["1", 1]), [1, "1"])

if __name__ == "__main__":
    unittest.main()
