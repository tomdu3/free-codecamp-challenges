def repeat_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    new_s = ''
    for letter in s:
        new_s += letter
        if letter.lower() in vowels:
            new_s += letter.lower() * count
            count +=1
    return new_s