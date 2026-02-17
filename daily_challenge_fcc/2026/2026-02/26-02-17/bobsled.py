def check_eligibility(athlete_weights, sled_weight):
    sled_min_weights = {
        1: 162,
        2: 170,
        4: 210,
    }

    sled_max_weights = {
        1: 247,
        2: 390,
        4: 630,
    }
    sled = len(athlete_weights)
    total_weight = sum(athlete_weights) + sled_weight
    if sled_min_weights[sled] > sled_weight or sled_max_weights[sled] < total_weight:
        return "Not Eligible"

    return "Eligible"
