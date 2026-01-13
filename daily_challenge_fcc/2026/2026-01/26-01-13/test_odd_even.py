import unittest

from odd_even import odd_or_even

"""
1. odd_or_even(1) should return "Odd".
Waiting:2. odd_or_even(2) should return "Even".
Waiting:3. odd_or_even(13) should return "Odd".
Waiting:4. odd_or_even(196) should return "Even".
Waiting:5. odd_or_even(123456789) should return "Odd".
"""


class TestOddEven(unittest.TestCase):
    def test_odd_or_even(self):
        self.assertEqual(odd_or_even(1), "Odd")
        self.assertEqual(odd_or_even(2), "Even")
        self.assertEqual(odd_or_even(13), "Odd")
        self.assertEqual(odd_or_even(196), "Even")
        self.assertEqual(odd_or_even(123456789), "Odd")
