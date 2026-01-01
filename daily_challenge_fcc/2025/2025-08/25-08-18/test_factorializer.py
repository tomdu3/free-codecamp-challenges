from factorializer import factorial
import unittest

"""
Tests

Waiting: 1. factorial(0) should return 1.
Waiting: 2. factorial(5) should return 120.
Waiting: 3. factorial(20) should return 2432902008176640000.
"""
class TestFactorializer(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(20), 2432902008176640000)

if __name__ == '__main__':
    unittest.main()
