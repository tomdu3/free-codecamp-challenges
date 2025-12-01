def is_mirror(str1, str2):
    str1_fix, str2_fix = "", ""
    for ch in str1:
        if ch.isalpha():
            str1_fix += ch
    for ch in str2:
        if ch.isalpha():
            str2_fix += ch

    return str1_fix == str2_fix[::-1]
