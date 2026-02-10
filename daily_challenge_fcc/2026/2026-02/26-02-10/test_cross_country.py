from cross_country import get_relative_results
import unittest


"""
    Tests

    Waiting: 1. get_relative_results(["1:25:32", "1:26:10", "1:27:05"]) should return ["0", "+0:38", "+1:33"].
    Waiting: 2. get_relative_results(["1:00:01", "1:00:05", "1:00:10"]) should return ["0", "+0:04", "+0:09"].
    Waiting: 3. get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]) should return ["0", "+0:17", "+0:42", "+2:05"].
    Waiting: 4. get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]) should return ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"].
    Waiting: 5. get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]) should return ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"].
"""

class TestCrossCountry(unittest.TestCase):
    def test_get_relative_results(self):
        self.assertEqual(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]), ["0", "+0:38", "+1:33"])
        self.assertEqual(get_relative_results(["1:00:01", "1:00:05", "1:00:10"]), ["0", "+0:04", "+0:09"])
        self.assertEqual(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]), ["0", "+0:17", "+0:42", "+2:05"])
        self.assertEqual(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]), ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"])
        self.assertEqual(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]), ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"])


if __name__ == '__main__':
    unittest.main()
