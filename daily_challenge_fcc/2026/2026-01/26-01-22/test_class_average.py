from class_average import get_average_grade
import unittest


class TestClassAverage(unittest.TestCase):
    def test_get_average_grade(self):
        self.assertEqual(get_average_grade([92, 91, 90, 94, 89, 93]), "A-")
        self.assertEqual(get_average_grade([84, 89, 85, 100, 91, 88, 79]), "B+")
        self.assertEqual(get_average_grade([63, 69, 65, 66, 71, 64, 65]), "D")
        self.assertEqual(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]), "A+")
        self.assertEqual(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]), "C+")
        self.assertEqual(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]), "F")

if __name__ == '__main__':
    unittest.main()
