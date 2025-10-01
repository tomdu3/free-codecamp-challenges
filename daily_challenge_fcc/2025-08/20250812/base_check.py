import string
def is_valid_number(n, base):
    full_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)

    bases = {i+2:full_list[:i+2] for i in range(35)}

    for digit in n:
        if digit.lower() not in bases[base]:
            return False
    return True