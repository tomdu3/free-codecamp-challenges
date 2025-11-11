def count(string):
    """
    Given a string, return an array with the number of vowels and number of consonants in the string.
    -   Vowels consist of `a`, `e`, `i`, `o`, `u` in any case.
    -   Consonants consist of all other letters in any case.
    -   Ignore any non-letter characters.
    """
    letter_counts = [0, 0]
    for letter in string:
        if letter.lower() in "aeiou":
            letter_counts[0] += 1
        elif letter.lower().isalpha():
            letter_counts[1] += 1
    return letter_counts
