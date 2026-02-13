def get_fastest_speed(times):
    segments = {
        0: 320,
        1: 280,
        2: 350,
        3: 300,
        4: 250
    }
    speeds = [segments[i]/times[i] for i in range(len(times))]
    max_speed = max(speeds)
    segment = speeds.index(max_speed)
    return f"The luger's fastest speed was {max_speed:.2f} m/s on segment {segment+1}."
