def squares_with_three(n):
    count = 0
    for i in range(1, n + 1):
        if str(i ** 2).count('3') > 0:
            count += 1

    return count
