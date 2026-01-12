import unittest

from plant_crop import get_number_of_plants


class TestPlantCrop(unittest.TestCase):
    def test_get_number_of_plants(self):
        self.assertEqual(get_number_of_plants(1, "acres", "corn"), 4046)
        self.assertEqual(get_number_of_plants(2, "hectares", "lettuce"), 100000)
        self.assertEqual(get_number_of_plants(20, "acres", "soybeans"), 161874)
        self.assertEqual(get_number_of_plants(3.75, "hectares", "tomatoes"), 150000)
        self.assertEqual(get_number_of_plants(16.75, "acres", "tomatoes"), 271139)
