def tire_status(pressures_psi, range_bar):
    """Return an array of strings describing each tire's status."""

    BAR_PSI_RATIO = 14.5038
    low, top = range_bar
    pressures_bar = [p / BAR_PSI_RATIO for p in pressures_psi]
    pressures_status = list(map(lambda p: "Low" if p < low else "Good" if p < top else "High", pressures_bar))
    return pressures_status

if __name__ == "__main__":
    print(tire_status([32, 28, 35, 29], [2, 3]))  # ['Good', 'Low', 'Good', 'Low']
    print(tire_status([32, 28, 35, 30], [2, 2.3]))  # ['Good', 'Low', 'High', 'Good']
    print(tire_status([29, 26, 31, 28], [2.1, 2.5]))  # ['Low', 'Low', 'Good', 'Low']
    print(tire_status([31, 31, 30, 29], [1.5, 2]))  # ['High', 'High', 'High', 'Good']
    print(tire_status([30, 28, 30, 29], [1.9, 2.1]))  # ['Good', 'Good', 'Good', 'Good']

