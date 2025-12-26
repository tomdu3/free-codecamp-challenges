def sum_divisors(n):
    divisors = []
    for i in range(1, n//2+1):
        if n % i == 0:
            if i in divisors or n//i in divisors:
                continue
            divisors.append(i)
            divisors.append(n//i)
    return sum(divisors)

if __name__ == '__main__':
    print(sum_divisors(9348))  # 23520
    print(sum_divisors(549))  # 806
    print(sum_divisors(84))  # 224
    print(sum_divisors(28))  # 56
    print(sum_divisors(13))  # 14
    print(sum_divisors(6))  # 12
