def format_number(number):
    int_prefix, prefix, first_half, second_half = number[0], number[1:4], number[4:7], number[7:]
    return f"+{int_prefix} ({prefix}) {first_half}-{second_half}"