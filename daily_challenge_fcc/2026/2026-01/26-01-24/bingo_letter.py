def get_bingo_letter(n):
    if 61 <= n <= 75:
        return "O"
    elif 46 <= n <= 60:
        return "G"
    elif 31 <= n <= 45:
        return "N"
    elif 16 <= n <= 30:
        return "I"
    elif 1 <= n <= 15:
        return "B"

    return "Invalid Number"
