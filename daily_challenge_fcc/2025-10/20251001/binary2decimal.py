def to_decimal(binary):
    decimal = 0
    for position, b_num in enumerate(binary[::-1]):
        decimal += int(b_num) * 2**position
    return decimal
