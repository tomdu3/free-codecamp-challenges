def generate_slug(str):
    # remove extra characters
    new_str = ''
    prev_ch = None
    str = str.strip()
    for ch in str:
        if not (ch.isalpha() or ch.isdigit() or ch == ' '):
            continue
        if ch == ' ':
            if (ch, prev_ch) == (' ', ' '):
                continue
            prev_ch = ch
            ch = '%20'
        else:
            prev_ch = ch
        new_str += ch.lower()
        new_str.strip('%20')
    return new_str