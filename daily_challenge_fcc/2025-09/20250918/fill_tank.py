def cost_to_fill(tank_size, fuel_level, price_per_gallon):

    return f"${(tank_size - fuel_level) * price_per_gallon:.2f}"