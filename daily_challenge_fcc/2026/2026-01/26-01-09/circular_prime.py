def is_circular_prime(n: int) -> bool:
    """Return True if n is a circular prime, False otherwise."""
    if n <= 1:
        return False
    num = str(n)
    is_prime = True
    rotations = [num[i:] + num[:i] for i in range(len(num))]
    for p in rotations:
        for i in range(2, int(p)//2):
            if int(p) % i == 0:
                is_prime = False
                break
        if not is_prime:
            break

    return is_prime

if __name__ == '__main__':
    print(is_circular_prime(197))
    print(is_circular_prime(23))
    print(is_circular_prime(13))
    print(is_circular_prime(89))
    print(is_circular_prime(1193))
