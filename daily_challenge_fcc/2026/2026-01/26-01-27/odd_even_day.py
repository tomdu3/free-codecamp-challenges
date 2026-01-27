import datetime as dt


def odd_or_even_day(timestamp):
    date = dt.datetime.fromtimestamp(timestamp / 1000, dt.timezone.utc)
    day = date.day
    if day % 2 == 0:
        return "even"
    else:
        return "odd"
