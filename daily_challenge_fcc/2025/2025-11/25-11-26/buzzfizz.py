def fizz_buzz(n):
    result = []
    cases = {
        3: 'Fizz',
        5: 'Buzz',
    }

    for i in range(1, n + 1):
        temp = ''
        for k, v in cases.items():
            if i % k == 0:
                temp += v
        result.append(temp or i)
    return result

def is_fizz_buzz(arr):
    result = fizz_buzz(len(arr))
    return arr == result