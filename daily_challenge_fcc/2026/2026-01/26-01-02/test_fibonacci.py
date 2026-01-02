from fibonacci import nth_fibonacci
import unittest


class TestNthFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nth_fibonacci(4), 2)
    def test_2(self):
        self.assertEqual(nth_fibonacci(10), 34)
    def test_3(self):
        self.assertEqual(nth_fibonacci(15), 377)
    def test_4(self):
        self.assertEqual(nth_fibonacci(40), 63245986)
    def test_5(self):
        self.assertEqual(nth_fibonacci(75), 1304969544928657)

if __name__ == "__main__":
    unittest.main()
