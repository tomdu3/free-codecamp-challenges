def to_snake(camel):
    snake = ''
    for letter in camel:
        if letter.upper() == letter and letter.isalpha():
            snake += '_' + letter.lower()
        else:
            snake += letter
        print(snake)
    return snake

