def hex_to_decimal(hex):
    hex_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    decimal = 0
    for i, val in enumerate((hex[::-1])):
        decimal += int(hex_values.index(val))*16**i
    return decimal