import unittest
from infected import infected

class TestInfected(unittest.TestCase):

    def test_infected_one_day(self):
        self.assertEqual(infected(1), 2)

    def test_infected_three_days(self):
        self.assertEqual(infected(3), 6)

    def test_infected_eight_days(self):
        self.assertEqual(infected(8), 152)

    def test_infected_seventeen_days(self):
        self.assertEqual(infected(17), 39808)

    def test_infected_twenty_five_days(self):
        self.assertEqual(infected(25), 5217638)

if __name__ == '__main__':
    unittest.main()
