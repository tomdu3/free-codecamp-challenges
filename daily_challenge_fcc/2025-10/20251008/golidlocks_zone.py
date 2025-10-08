def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start_zone = round(0.95 * luminosity ** 0.5, 2)
    end_zone = round(1.37 * luminosity ** 0.5, 2)
    return [start_zone, end_zone]