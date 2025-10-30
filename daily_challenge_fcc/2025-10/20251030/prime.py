import functools

@functools.lru_cache(maxsize=None)
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    """Return the n-th prime number (1-indexed)."""
    if n < 1:
        raise ValueError("n must be a positive integer.")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate