def largest_difference(skater1, skater2):
    max_lap_diff = (0, 0)
    for index, (lap1, lap2) in enumerate(zip(skater1, skater2)):
        temp_lap_diff = abs(lap2 - lap1)
        if temp_lap_diff > max_lap_diff[1]:
            max_lap_diff = (index, temp_lap_diff)

    return max_lap_diff[0] + 1
