def string_sum(s: str) -> int:
    """Return the sum of all numbers in the string.

    Treat consecutive digits as a single number. For example, `"13"` counts as 13, not 1 + 3.
    Ignore any non-digit characters.
    """
    if len(s) == 0:
        return 0
    total = 0
    num_str = ""
    prev_char = None
    for idx, ch in enumerate(s):
        if ch.isdigit():
            if prev_char is None:
                num_str = ch
            else:
                num_str += ch
            prev_char = ch
        elif num_str != "":
            total += int(num_str)
            num_str = ""
            prev_char = None
    if num_str != "":
        total += int(num_str)
    return total
