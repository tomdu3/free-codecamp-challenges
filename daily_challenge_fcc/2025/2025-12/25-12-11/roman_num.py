def to_roman(num):
    """
    Convert an integer to a Roman numeral.

    Args:
        num (int): The integer to convert.
    
    Returns:
        str: The Roman numeral representation of the integer.
    """
        # Define value-symbol pairs including subtractive cases
    value_symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    result = ""
    
    # Process each value from largest to smallest
    for value, symbol in value_symbols:
        # Count how many times this value fits into the current number
        count = num // value
        
        if count > 0:
            # Add the symbol that many times
            result += symbol * count
            # Reduce the number by the value we've processed
            num -= value * count
            
        # If we've processed the entire number, break early
        if num == 0:
            break
    
    return result

if __name__ == "__main__":
    print(to_roman(18))   # XVIII
    print(to_roman(19))   # XIX
    print(to_roman(1464)) # MCDLXIV
    print(to_roman(2025)) # MMXXV
    print(to_roman(3999)) # MMMCMXCIX
    # Additional test cases
    print(to_roman(4))    # IV
    print(to_roman(9))    # IX
    print(to_roman(44))   # XLIV
    print(to_roman(99))   # XCIX
    print(to_roman(1989))  # MCMLXXXIX