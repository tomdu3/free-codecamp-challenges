def to_12(time):
    """
    Given a string representing a time of the day in the 24-hour format of "HHMM",
    return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
    """

    hours = int(time[:2])
    minutes = time[2:]

    period = "AM" if hours < 12 else "PM"
    hours %= 12
    if hours == 0:
        hours = 12
    time = f"{hours}:{minutes} {period}"

    return time