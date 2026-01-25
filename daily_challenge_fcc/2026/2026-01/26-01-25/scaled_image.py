def scaled_image(size, scale):
    width, height = (int(x) for x in size.split("x"))
    return f"{int(width * scale)}x{int(height * scale)}"
