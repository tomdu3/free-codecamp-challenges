import datetime as dt
def calculate_age(birth_date: str) -> int:
    birth_date = dt.datetime.strptime(birth_date, "%Y-%m-%d")
    today = dt.datetime.now()
    birthday_celebrated_diff = 0 if today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day) else 1
    age = today.year - birth_date.year - birthday_celebrated_diff
    return age