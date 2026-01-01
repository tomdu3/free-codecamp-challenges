def jbelmu(text):
    words = text.split()
    new_text = []
    for word in words:
        if len(word) <= 2:
            new_text.append(word)
        else:
            first_letter = word[0]
            last_letter = word[-1]
            sorted_letters = ''.join(sorted(list(word[1:-1])))
            new_text.append(first_letter + sorted_letters + last_letter)
            
    text = ' '.join(new_text)
    return text
