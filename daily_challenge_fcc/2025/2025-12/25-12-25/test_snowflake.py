from snowflake import generate_snowflake
import unittest


class TestSnowflake(unittest.TestCase):
    def test_generate_snowflake(self):
        self.assertEqual(generate_snowflake("* \n *\n* "), "*  *\n ** \n*  *")
    def test_generate_snowflake_no_spaces(self):
        self.assertEqual(generate_snowflake("X=~"), "X=~~=X")
    def test_generate_snowflake_with_spaces_and_special_chars(self):
        self.assertEqual(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "), " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ")
    def test_generate_snowflake_with_spaces2(self):
        self.assertEqual(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"), "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *")
    def test_generate_snowflake_with_spaces_and_minus(self):
        self.assertEqual(generate_snowflake("*  -\n * -\n*  -"), "*  --  *\n * -- * \n*  --  *")

if __name__ == '__main__':
    unittest.main()
