def one_hundred(chars):
    times = 100 // len(chars)


    return chars * times + chars[:100 % len(chars)]