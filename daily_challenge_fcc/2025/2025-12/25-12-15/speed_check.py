def speed_check(speed_mph, speed_limit_kph):
    mph_to_kph =1.60934
    speed_kph = speed_mph * mph_to_kph

    if speed_kph <= speed_limit_kph:
        return "Not Speeding"
    elif speed_kph <= speed_limit_kph + 5:
        return "Warning"
    else:
        return "Ticket"