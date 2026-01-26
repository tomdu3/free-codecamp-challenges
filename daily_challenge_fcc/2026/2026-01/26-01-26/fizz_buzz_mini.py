def fizz_buzz_mini(n):
    res = ""
    if n % 3 == 0:
        res += "Fizz"
    if n % 5 == 0:
        res += "Buzz"
    if n % 3 and n % 5:
        res = str(n)
    return res
