def is_unnatural_prime(n):
    if abs(n) < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if abs(n) % i == 0:
            return False
    return True