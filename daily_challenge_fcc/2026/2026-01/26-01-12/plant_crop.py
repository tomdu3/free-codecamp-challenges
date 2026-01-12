def get_number_of_plants(field_size, unit, crop):
    units = {"acres": 4046.86, "hectares": 10_000}

    crops = {"corn": 1, "wheat": 0.1, "soybeans": 0.5, "tomatoes": 0.25, "lettuce": 0.2}

    if crop not in crops:
        raise ValueError("Invalid crop")
    crop_yield = crops[crop]

    if unit not in units:
        raise ValueError("Invalid unit")
    field_size = field_size * units[unit]

    number_of_plants = int(field_size / crop_yield)

    return number_of_plants


if __name__ == "__main__":
    print(get_number_of_plants(1, "acres", "corn"))
    print(get_number_of_plants(2, "hectares", "lettuce"))
    print(get_number_of_plants(20, "acres", "soybeans"))
    print(get_number_of_plants(3.75, "hectares", "tomatoes"))
    print(get_number_of_plants(16.5, "acres", "tomatoes"))
