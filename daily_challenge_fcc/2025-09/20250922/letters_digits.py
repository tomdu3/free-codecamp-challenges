def digits_or_letters(s):

    letters = []
    digits = []
    for ch in s.lower():
        if ch.isdigit():
            digits.append(ch)
        elif ch.isalpha():
            letters.append(ch)
    
    len_digits = len(digits)
    len_letters = len(letters)

    if len_digits == len_letters:
        message = 'tie'
    elif len_digits > len_letters:
        message = 'digits'
    else:
        message = 'letters'
    return message