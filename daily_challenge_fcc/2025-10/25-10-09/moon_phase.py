from datetime import datetime
def moon_phase(date_string):
    LUNAR_PHASES = {
    "New": (1, 7),
    "Waxing": (8, 14),
    "Full": (15, 21),
    "Waning": (22, 28)
    }
    REFERENCE_DATE = datetime.strptime('2000-01-06', '%Y-%m-%d')
    
    date = datetime.strptime(date_string, '%Y-%m-%d')
    days_difference = (date - REFERENCE_DATE).days
    lunar_day = days_difference % 28 + 1
    for phase, (start, end) in LUNAR_PHASES.items():
        if start <= lunar_day <= end:
            return phase
    return 'Error'