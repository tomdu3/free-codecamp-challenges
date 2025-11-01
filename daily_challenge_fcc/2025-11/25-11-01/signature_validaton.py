import string
def sum_of_letters(message):
    alphabet = string.ascii_letters
    sum_message = 0
    for letter in message:
        if letter in alphabet:
            sum_message += alphabet.index(letter)+1
    return sum_message

def verify(message, key, signature):
    
    return sum_of_letters(message) + sum_of_letters(key) == signature

