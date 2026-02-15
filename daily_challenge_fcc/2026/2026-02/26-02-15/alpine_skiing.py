def get_hill_rating(drop, distance, hill_type):
    hill_types = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0,
    }

    steepness = drop / distance * hill_types[hill_type]

    if steepness <= 0.1:
        return "Green"
    elif steepness <= 0.25:
        return "Blue"
    else:
        return "Black"
