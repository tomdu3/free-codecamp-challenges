from functools import cache

@cache
def nth_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n-1 <= 1:
       return n-1
    else:
       return(nth_fibonacci(n-1) + nth_fibonacci(n-2))


if __name__ == "__main__":
    print(nth_fibonacci(4))
    print(nth_fibonacci(10))
    print(nth_fibonacci(15))
    print(nth_fibonacci(40))
    print(nth_fibonacci(75))
