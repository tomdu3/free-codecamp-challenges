import random
def generate_hex(color):
    colors = [0,0,0]
    while len(colors) != len(set(colors)):
        colors = sorted([random.randint(0, 255) for _ in range(3)])
    hex = [0, 0, 0]
    if color == "red":
        hex[0] = colors[2]
        hex[1] = colors[0]
        hex[2] = colors[1]
    elif color == "green":
        hex[1] = colors[2]
        hex[0] = colors[1]
        hex[2] = colors[0]
    elif color == "blue":
        hex[2] = colors[2]
        hex[0] = colors[0]
        hex[1] = colors[1]
    else:
        return "Invalid color"

    return f"{hex[0]:02x}{hex[1]:02x}{hex[2]:02x}"
