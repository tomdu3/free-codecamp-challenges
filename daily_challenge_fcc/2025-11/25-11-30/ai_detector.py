def detect_ai(text):
    if text.count("-") >= 2:
        return "AI"

    if text.count("(") >= 2 and text.count(")") >= 2:
        return "AI"
    
    list_of_words = text.split(" ")
    if len(list_of_words)>= 3:
        count = 0
        for word in list_of_words:
            if len(
                    word.replace("-", "").replace("(", "")
                    .replace(")", "").replace(" ", "")
                    .replace(",", "").replace(".", "")
                    .replace("?", "").replace("!", "")
                   ) >= 7:
                count += 1
        if count >= 3:
            return "AI"
    
    return "Human"
