def scale_recipe(ingredients, scale):
    new_ingredients = []
    for ingredient in ingredients:
         quantity, unit, *name = ingredient.split()
         new_quantity = float(quantity) * scale
         new_ingredients.append(f"{new_quantity if new_quantity % 1 != 0 else int(new_quantity)} {unit} {' '.join(name)}")
    return new_ingredients
