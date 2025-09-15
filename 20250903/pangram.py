def is_pangram(sentence, letters):
    sentence_letters = set([letter.lower() for letter in sentence if letter.isalpha()])
    return sorted(sentence_letters) == sorted(letters)