def separate_letters_and_numbers(s):
    prev = None
    result = ""

    for char in s:
        if prev is None:
            prev = char
        elif char.isalpha() != prev.isalpha():
            result += "-"
        result += char
        prev = char

    return result