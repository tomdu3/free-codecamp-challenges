def is_valid_message(message, validation):
    message = message.lower()
    validation = validation.lower()
    if len(message.split()) != len(validation):
        return False
    for word, letter in zip(message.split(), validation):
        if word[0] != letter:
            return False
    return True
