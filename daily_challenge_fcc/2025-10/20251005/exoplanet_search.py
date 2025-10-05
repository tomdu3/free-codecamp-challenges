import string

def has_exoplanet(readings):
    # List of digits 0-9
    digits = list(string.digits)

    # List of uppercase letters A-Z
    letters = list(string.ascii_uppercase)

    # Combine the lists
    readings_levels = digits + letters
    print(readings_levels)
    


    average = sum([readings_levels.index(reading) for reading in readings])/len(readings)
    print(average)

    for reading in readings:
        if readings_levels.index(reading) <= .80 * average:
            return True

    return False

print(has_exoplanet("665544554"))  # False