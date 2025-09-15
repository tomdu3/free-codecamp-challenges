def rgb_to_hex(rgb):
    rgb_list = rgb.lstrip('rgb(').rstrip(')').split(',')
    hex_num = '#'
    for num in rgb_list:
        conv_num = hex(int(num)).lstrip('0x')
        if len(conv_num) < 2: conv_num = '0'+conv_num
        hex_num += conv_num
    return hex_num