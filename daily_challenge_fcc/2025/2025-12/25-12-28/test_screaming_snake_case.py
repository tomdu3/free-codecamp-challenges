from screaming_snake_case import to_screaming_snake_case 
import unittest

"""
Tests

Waiting: 1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
Waiting: 2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
Waiting: 3. to_screaming_snake_case("user_id") should return "USER_ID".
Waiting: 4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
Waiting: 5. to_screaming_snake_case("username") should return "USERNAME".
"""

class TestScreamingSnakeCase(unittest.TestCase):
    def test_to_screaming_snake_case(self):
        self.assertEqual(to_screaming_snake_case("userEmail"), "USER_EMAIL")
        self.assertEqual(to_screaming_snake_case("UserPassword"), "USER_PASSWORD")
        self.assertEqual(to_screaming_snake_case("user_id"), "USER_ID")
        self.assertEqual(to_screaming_snake_case("user-address"), "USER_ADDRESS")
        self.assertEqual(to_screaming_snake_case("username"), "USERNAME")

if __name__ == "__main__":
    unittest.main()