def check_strength(password):
    length = False
    lower_case = False
    upper_case = False
    number = False
    special = False
    if len(password) >= 8:
        length = True
    for letter in password:
        if letter.isalpha():
            if letter == letter.lower() and not lower_case:
                lower_case = True
            elif letter == letter.upper() and not upper_case:
                upper_case = True
        elif letter.isdigit() and not number:
            number = True
        elif letter in [ '!', '@', '#', '$', '%', '^', '&', '*'] and not special:
            special = True
    
    rules = sum([1 for rule in [length, lower_case and upper_case, number, special] if rule is True])

    if rules < 2:
        return 'weak'
    elif rules < 4:
        return 'medium'
    return 'strong'