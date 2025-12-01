import unittest
from decimal2binary import to_binary


class TestDecimal2Binary(unittest.TestCase):
    def test_to_binary(self):
        self.assertEqual(to_binary(5), "101")
        self.assertEqual(to_binary(12), "1100")
        self.assertEqual(to_binary(50), "110010")
        self.assertEqual(to_binary(99), "1100011")
