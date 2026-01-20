def to_consonant_case(string):
    vowels = "aeiou"
    result = ""
    for ch in string:
        if ch.isalpha():
            if ch.lower() in vowels:
                result += ch.lower()
            else:
                result += ch.upper()
        elif ch == "-":
            result += "_"
        else:
            result += ch
    return result

