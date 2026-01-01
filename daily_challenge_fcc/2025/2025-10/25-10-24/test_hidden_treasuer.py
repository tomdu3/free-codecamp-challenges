import unittest
from hidden_treasure import dive

class TestHiddenTreasure(unittest.TestCase):
    def test_cases(self):
        # Test case 1: Should return "Recovered"
        self.assertEqual(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]), "Recovered")
        # Test case 2: Should return "Empty"
        self.assertEqual(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]), "Empty")
        # Test case 3: Should return "Found"
        self.assertEqual(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]), "Found")
        # Test case 4: Should return "Found"
        self.assertEqual(dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]), "Found")
        # Test case 5: Should return "Recovered"
        self.assertEqual(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]), "Recovered")
        # Test case 6: Should return "Empty"
        self.assertEqual(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]), "Empty")

if __name__ == '__main__':
    unittest.main()