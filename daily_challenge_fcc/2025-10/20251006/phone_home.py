def send_message(route):
    LIGHT_SPEED = 300000
    time = 0.0
    for index, distance in enumerate(route):
        # each satellite passed (every stop except the starting point) adds 0.5s
        delay = 0.5 if index != 0 else 0.0

        # travel time for this segment is distance (km) divided by light speed (km/s)
        time += distance / LIGHT_SPEED + delay

    return round(time, 4)