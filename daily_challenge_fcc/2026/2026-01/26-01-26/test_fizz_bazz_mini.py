from fizz_buzz_mini import fizz_buzz_mini
import unittest

"""
tests:
fizz_buzz_mini(3) should return "Fizz"
fizz_buzz_mini(4) should return "4"
fizz_buzz_mini(35) should return "Buzz"
fizz_buzz_mini(75) should return "FizzBuzz"
fizz_buzz_mini(98) should return "98"
"""


class TestFizzBuzzMini(unittest.TestCase):
    def test_fizz_buzz_mini(self):
        self.assertEqual(fizz_buzz_mini(3), "Fizz")
        self.assertEqual(fizz_buzz_mini(4), "4")
        self.assertEqual(fizz_buzz_mini(35), "Buzz")
        self.assertEqual(fizz_buzz_mini(75), "FizzBuzz")
        self.assertEqual(fizz_buzz_mini(98), "98")


if __name__ == "__main__":
    unittest.main()
