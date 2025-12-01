def is_spam(number):
    country_code, area_code, local_number = number.split()
    country_code = country_code.replace('+', '')
    area_code = area_code.replace('(', '').replace(')', '')
    local_first, local_second = local_number.split('-')

    print(country_code + area_code + local_first + local_second)

    if len(country_code) > 2 or not country_code.startswith('0'):
        return True
    elif not 200 <= int(area_code) <= 900:
        return True
    elif str(sum([int(num) for num in local_first])) in local_second:
        return True
    
    prev = ''
    for num in country_code + area_code + local_first + local_second:
        if prev == num:
            count += 1
            if count >= 4:
                return True
        else:
            count = 1
        prev = num

    return False

print(is_spam("+0 (555) 564-1987"))