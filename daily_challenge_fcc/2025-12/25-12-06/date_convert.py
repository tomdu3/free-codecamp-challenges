import datetime as dt
def format_date(date_string):
    date, year = date_string.split(",")
    date = date.strip()
    month, day = date.split(" ")
    year = year.strip()
    month_str = dt.datetime.strptime(month, "%B").strftime("%m")
    if int(day) < 10:
        day = f"0{day}"
    return f"{year}-{month_str}-{day}"

