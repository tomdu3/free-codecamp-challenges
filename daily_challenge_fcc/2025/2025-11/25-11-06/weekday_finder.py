import datetime as dt


def get_weekday(date_string):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    date = dt.datetime.strptime(date_string, "%Y-%m-%d")
    date = date.weekday()

    return days[date]
