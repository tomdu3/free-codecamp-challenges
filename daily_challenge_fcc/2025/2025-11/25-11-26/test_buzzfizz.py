import unittest
from buzzfizz import fizz_buzz, is_fiz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_15(self):
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
        self.assertEqual(fizz_buzz(15), expected)

    def test_fizz_buzz_5(self):
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(fizz_buzz(5), expected)

    def test_fizz_buzz_1(self):
        expected = [1]
        self.assertEqual(fizz_buzz(1), expected)

    def test_is_fizz_buzz_true_short(self):
        self.assertTrue(is_fiz_buzz([1, 2, "Fizz", 4, "Buzz"]))

    def test_is_fizz_buzz_true_long(self):
        self.assertTrue(is_fiz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))

    def test_is_fizz_buzz_false_incorrect_fizz(self):
        self.assertFalse(is_fiz_buzz([1, 2, 3, 4]))