def compare(word, guess):
    used_guesses = []
    result = [0] *  len(word)
    for i, letter in enumerate(word):
        if letter == guess[i]:
            result[i] = 2
            used_guesses.append(letter)

    for i, letter in enumerate(guess):
        if letter == word[i]:
            continue
        if letter in word:
            if letter in used_guesses and \
                word.count(letter) > used_guesses.count(letter) \
                    or letter not in used_guesses:
                result[i] = 1
                used_guesses.append(letter)
        else:
            result[i] = 0
    return ''.join(map(str, result))