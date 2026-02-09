from ski_jumping import ski_jump_medal
import unittest


class TestSkiJumping(unittest.TestCase):

    def test_ski_jump_medal(self):
        self.assertEqual(ski_jump_medal(125.0, 58.0, 0.0, 6.0), 'Gold')
        self.assertEqual(ski_jump_medal(119.0, 50.0, 1.0, 4.0), 'Bronze')
        self.assertEqual(ski_jump_medal(122.0, 52.0, -1.0, 4.0), 'Silver')
        self.assertEqual(ski_jump_medal(118.0, 50.5, -1.5, 4.0), 'No Medal')
        self.assertEqual(ski_jump_medal(124.0, 50.5, 2.0, 5.0), 'Gold')
        self.assertEqual(ski_jump_medal(119.0, 49.5, 0.0, 3.0), 'No Medal')

if __name__ == '__main__':
    unittest.main()
