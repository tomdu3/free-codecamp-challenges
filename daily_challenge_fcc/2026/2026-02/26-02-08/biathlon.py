def calculate_penalty_distance(rounds):
    penalty_distance = 0
    for round in rounds:
        penalty_distance += (5 - round) * 150
    return penalty_distance
