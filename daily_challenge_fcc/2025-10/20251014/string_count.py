def count(text, parameter):
    count = 0
    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            count += 1
    return count
    
