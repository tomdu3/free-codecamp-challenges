import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_factors(x):
    factors = []
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def check_factor(x, factor):
    count = 0
    while x % factor == 0 and x != 0:
        x //= factor
        count += 1
    return count


def lcm(a, b):
    factors_a = [factor for factor in prime_factors(a) for _ in range(check_factor(a, factor))]
    factors_b = [factor for factor in prime_factors(b) for _ in range(check_factor(b, factor))]
    print(factors_a)
    print(factors_b)
    common_factors = set(factors_a + factors_b)
    print(common_factors)
    lcm = 1
    for factor in common_factors:
        lcm *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    return lcm
