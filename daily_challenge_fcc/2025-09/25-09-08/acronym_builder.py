def build_acronym(string):
    ingnored_words = ["a", "for", "an", "and", "by", "of"]
    acronym = ""
    words = string.split()
    for word in words:
        if word not in ingnored_words or word == words[0]:
            acronym += word[0].upper()
    return acronym