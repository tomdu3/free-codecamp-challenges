import datetime as dt
def days_until_weekend(date_string):
    date = dt.datetime.strptime(date_string, "%Y-%m-%d").date()
    day_num = date.weekday()
    if day_num >= 5:
        return "It's the weekend!"
    else:
        days_to_weekend = 5 - day_num
        return f"{days_to_weekend} day{'s' if days_to_weekend > 1 else ''} until the weekend."
