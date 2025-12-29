def too_much_screen_time(hours):
    if max(hours) >= 10:
        return True
    total = 0
    three_days = []
    for i, hour in enumerate(hours):
        total += hour
        if i >= 2:
            three_days.append(hour)
            if len(three_days) == 3:
                if sum(three_days) / 3 >= 8:
                    return True
                three_days.pop(0)
        else:
            three_days.append(hour)
    if total / 7 >= 6:
        return True
    return False
        