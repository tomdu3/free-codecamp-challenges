def can_post(message):
    message_length = len(message)
    if message_length <= 40:
        return "short post"
    elif message_length > 40 and message_length <= 80:
        return "long post"
    else:
        return "invalid post"
