def count_rectangles(width, height):
    total_rectangles = width * (width + 1) * height * (height + 1) // 4
    
    return total_rectangles