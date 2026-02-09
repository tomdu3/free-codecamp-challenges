def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    other_jumpers = [
        165.5,
        172.0,
        158.0,
        180.0,
        169.5,
        175.0,
        162.0,
        170.0
    ]

    medals = {
        0: 'Gold',
        1: 'Silver',
        2: 'Bronze',
    }

    total = distance_points + style_points + wind_comp + k_point_bonus

    other_jumpers.append(total)

    position = sorted(other_jumpers, reverse=True).index(total)

    return medals[position] if position < 3 else 'No Medal'
