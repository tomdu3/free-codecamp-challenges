def is_integer_hypotenuse(a: int, b: int) -> bool:
    c = (a ** 2 + b ** 2) ** 0.5
    return int(c) == c