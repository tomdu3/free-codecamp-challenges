from int_hypotenuse import is_integer_hypotenuse
import unittest


class TestIntegerHypotenuse(unittest.TestCase):
    def test_is_integer_hypotenuse(self):
        self.assertEqual(is_integer_hypotenuse(3, 4), True)
        self.assertEqual(is_integer_hypotenuse(2, 3), False)
        self.assertEqual(is_integer_hypotenuse(5, 12), True)
        self.assertEqual(is_integer_hypotenuse(10, 10), False)
        self.assertEqual(is_integer_hypotenuse(780, 1040), True)
        self.assertEqual(is_integer_hypotenuse(250, 333), False)

if __name__ == '__main__':
    unittest.main()
