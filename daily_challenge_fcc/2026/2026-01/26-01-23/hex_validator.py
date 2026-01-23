def is_valid_hex(s):
    if s[0] != '#':
        return False
    if len(s[1:]) not in [3, 6]:
        return False
    
    for char in s[1:]:
        if ord(char.upper()) not in range(ord('0'), ord('9') + 1) and ord(char.upper()) not in range(ord('A'), ord('F') + 1):
            return False
    
    return True