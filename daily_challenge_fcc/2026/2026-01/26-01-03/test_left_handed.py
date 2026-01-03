from left_handed import find_left_handed_seats
import unittest

"""
Tests
Waiting:1. find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]) should return 2.
Waiting:2. find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]) should return 8.
Waiting:3. find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]) should return 0.
Waiting:4. find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]) should return 1.
Waiting:5. find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]) should return 5.
"""

class TestLeftHanded(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]), 2)

    def test_2(self):
        self.assertEqual(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]), 8)

    def test_3(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]), 0)

    def test_4(self):
        self.assertEqual(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]), 1)

    def test_5(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]), 5)

if __name__ == '__main__':
    unittest.main()
