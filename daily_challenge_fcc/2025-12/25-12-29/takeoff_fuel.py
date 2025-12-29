import math
def fuel_to_add(current_gallons, required_liters):
    GALLON_TO_LITERS = 3.78541
    required_gallons = math.ceil(required_liters / GALLON_TO_LITERS)
    if current_gallons >= required_gallons:
        return 0
    return required_gallons - current_gallons
