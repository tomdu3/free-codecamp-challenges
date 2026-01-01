import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(2), [1, 2])

    def test_fizz_buzz_4(self):
        self.assertEqual(fizz_buzz(4), [1, 2, "Fizz", 4])

    def test_fizz_buzz_8(self):
        self.assertEqual(fizz_buzz(8), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8])

    def test_fizz_buzz_20(self):
        expected_output = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"
        ]
        self.assertEqual(fizz_buzz(20), expected_output)

    def test_fizz_buzz_50(self):
        expected_output = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
            "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz",
            31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz",
            41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"
        ]
        self.assertEqual(fizz_buzz(50), expected_output)
