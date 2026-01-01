conversion_table = {
    -90: 24,
    -75: 23,
    -60: 21,
    -45: 15,
    -30: 13,
    -15: 12,
    0: 12,
    15: 11,
    30: 10,
    45: 9,
    60: 6,
    75: 2,
    90: 0
    }

def daylight_hours(latitude):
    if latitude in conversion_table:
        return conversion_table[latitude]
    
    latitudes = list(conversion_table.keys())
    latitudes.sort()
    
    for i in range(len(latitudes) - 1):
        if latitudes[i] < latitude < latitudes[i + 1]:
            closest_latitude = min(conversion_table.keys(), key=lambda lat: abs(lat - latitude))
            return conversion_table[closest_latitude]