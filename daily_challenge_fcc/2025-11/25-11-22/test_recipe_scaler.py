import unittest
from recipe_scaler import scale_recipe

class TestRecipeScaler(unittest.TestCase):

    def test_scale_recipe_simple_doubling(self):
        ingredients = ["2 C Flour", "1.5 T Sugar"]
        scale = 2
        expected_output = ["4 C Flour", "3 T Sugar"]
        self.assertEqual(scale_recipe(ingredients, scale), expected_output)

    def test_scale_recipe_with_decimal_scale(self):
        ingredients = ["4 T Flour", "1 C Milk", "2 T Oil"]
        scale = 1.5
        expected_output = ["6 T Flour", "1.5 C Milk", "3 T Oil"]
        self.assertEqual(scale_recipe(ingredients, scale), expected_output)

    def test_scale_recipe_halving(self):
        ingredients = ["3 C Milk", "2 C Oats"]
        scale = 0.5
        expected_output = ["1.5 C Milk", "1 C Oats"]
        self.assertEqual(scale_recipe(ingredients, scale), expected_output)

    def test_scale_recipe_complex_recipe(self):
        ingredients = ["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"]
        scale = 2.5
        expected_output = ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar", "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"]
        self.assertEqual(scale_recipe(ingredients, scale), expected_output)

if __name__ == '__main__':
    unittest.main()
