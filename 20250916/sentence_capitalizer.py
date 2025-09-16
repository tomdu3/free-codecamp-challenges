def capitalize(paragraph):
    sentence_endings = ['.', '!', '?']
    para = ''
    capitalize_letter = True
    for letter in paragraph:
        if capitalize_letter and letter.isalpha():
            letter = letter.upper()
            capitalize_letter = False
        elif letter in sentence_endings:
            capitalize_letter = True

        para += letter

    return para