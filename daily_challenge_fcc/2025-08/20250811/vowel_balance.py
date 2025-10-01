def is_balanced(s):
    vowels = 'aeiou'
    mid = len(s)//2
    s = s.lower()

    
    if len(s) % 2 == 0:
        first_half_end = mid
        second_half_start = mid
    else:
        first_half_end = mid
        second_half_start = mid + 1
    
    first_half_count = len([ch for ch in s[:first_half_end] if ch in vowels])
    second_half_count = len([ch for ch in s[second_half_start:] if ch in vowels])

    return first_half_count == second_half_count
    
    