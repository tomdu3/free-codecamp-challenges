from most_frequent import most_frequent
import unittest

class TestMostFrequent(unittest.TestCase):
    def test_most_frequent(self):
        self.assertEqual(most_frequent(["a", "b", "a", "c"]), "a")
        self.assertEqual(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]), 2)
        self.assertEqual(most_frequent([True, False, "False", "True", False]), False)
        self.assertEqual(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]), 40)

if __name__ == "__main__":
    unittest.main()


        