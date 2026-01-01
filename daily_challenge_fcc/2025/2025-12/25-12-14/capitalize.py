def title_case(title):
    new_title = []
    for word in title.split(" "):
        new_title.append(word[0].upper() + word[1:].lower())
    return " ".join(new_title)