def spookify(boo):
    print(boo)
    trans_table = str.maketrans('-_', '~~')
    string = boo.translate(trans_table)
    print(string)
    new_string = ''
    count = 0
    for ch in string:
        print(ch)
        if ch == '~':
            new_string += ch 
        else:
            count += 1
            if count % 2 != 0:
                new_string += ch.upper()
            else:
                new_string += ch.lower()
    return new_string