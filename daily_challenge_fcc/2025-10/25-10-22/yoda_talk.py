def wise_speak(sentence):
    words = ["have", "must","are", "will", "can"]
    for word in words:
        if word in sentence:
            index = sentence.index(word)
            first, second = [sentence[:index+len(word)], sentence[index+len(word)+1:-1].strip()]
            sentence = second.capitalize() + ", " + first[0][0].lower()+first[1:] + sentence[-1]
    return sentence