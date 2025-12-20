from purge_most_frequent import purge_most_frequent
import unittest

class TestPurgeMostFrequent(unittest.TestCase):
    def test_1(self):
        self.assertEqual(purge_most_frequent([1, 2, 2, 3]), [1, 3])
    
    def test_2(self):
        self.assertEqual(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]), ["a", "b", "b", "c", "c", "c"])
    
    def test_3(self):
        self.assertEqual(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]), ["red", "green", "red", "green"])
    
    def test_4(self):
        self.assertEqual(purge_most_frequent([5, 5, 5, 5]), [])

if __name__ == "__main__":
    unittest.main()