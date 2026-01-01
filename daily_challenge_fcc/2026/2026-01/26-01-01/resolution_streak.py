def resolution_streak(days):
    streak = 0
    failed_day = None
    message = ""
    for idx, day in enumerate(days):
        if day[0] < 10000 or day[1] > 120 or day[2] < 5:
            failed_day = idx + 1
            message = "Resolution failed on day {}: {} day streak.".format(failed_day, streak)
            break
        else:
            streak += 1
            message = "Resolution on track: {} day streak.".format(streak)
    return message

