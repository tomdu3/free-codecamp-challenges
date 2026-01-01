import math

def adjust_thermostat(current_f, target_c):
    target_f = target_c * 1.8 + 32

    difference = target_f - current_f
    if difference > 0:
        return f'Heat: {difference:.1f} degrees Fahrenheit'
    elif difference < 0:
        return f'Cool: {abs(difference):.1f} degrees Fahrenheit'
    else:
        return 'Hold'