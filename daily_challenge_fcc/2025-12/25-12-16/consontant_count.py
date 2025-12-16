def has_consonant_count(text, target):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() not in vowels and char.isalpha():
            count += 1
    return count >= target